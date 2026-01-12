# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_13:09:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,596 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 13:09:03 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:08:50 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-01-12 13:08:24 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:08:15 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:07:04 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-01-12 13:06:41 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:06:14 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:06:10 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:06:06 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 13:05:08 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-12 13:04:16 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.107 |  |
| 2026-01-12 13:03:27 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.077 |  |
| 2026-01-12 13:03:25 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.051 |  |
| 2026-01-12 13:03:23 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.070 |  |
| 2026-01-12 13:03:04 | Yaka Wewa (Ma Oya) | 2.78 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-01-12 13:03:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-01-12 13:02:41 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-12 13:02:33 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 13:02:17 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:02:10 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:02:03 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-12 13:01:55 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-12 13:01:46 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-12 13:01:44 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:43 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:39 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 13:01:35 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 13:01:25 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:20 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:12 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:12 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:00:46 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.119 |  |
| 2026-01-12 13:00:05 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:13:40 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.107 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 13:03:04 | Yaka Wewa (Ma Oya) | 2.78 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-01-12 13:05:08 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-01-12 13:01:46 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-12 13:01:55 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-12 13:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 13:01:35 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 13:01:39 | Weraganthota (Mahaweli Ganga) | -1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 13:06:06 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 13:02:10 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:02:33 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:43 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:12 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:02:17 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:00:05 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:07:18 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:06:10 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:20 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:12 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:08:24 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:06:14 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 12:03:26 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:09:03 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:08:15 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:01:25 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:06:41 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 13:08:50 | Giriulla (Maha Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-01-12 13:07:04 | Manampitiya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-01-12 13:02:03 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-01-12 12:02:58 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-01-12 13:02:41 | Magura (Kalu Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-01-12 12:01:46 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-01-12 12:02:33 | Peradeniya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.033 |  |
| 2026-01-12 12:05:53 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.048 |  |
| 2026-01-12 13:03:25 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | -0.051 |  |
| 2026-01-12 13:03:02 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.059 |  |
| 2026-01-12 13:03:23 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | -0.070 |  |
| 2026-01-12 13:03:27 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | -0.077 |  |
| 2026-01-12 13:04:16 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | -0.107 |  |
| 2026-01-12 13:00:46 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)