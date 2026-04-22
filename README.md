# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_09:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 09:12:00 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.018 |  |
| 2026-04-22 09:10:10 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:10:08 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-22 09:07:16 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-04-22 09:06:51 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-22 09:06:49 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:06:36 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.043 |  |
| 2026-04-22 09:06:25 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 09:06:18 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:05:34 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.058 |  |
| 2026-04-22 09:05:31 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.124 |  |
| 2026-04-22 09:05:08 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-22 09:05:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:05:00 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:03:52 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-22 09:03:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:03:20 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.032 |  |
| 2026-04-22 09:03:16 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:03:13 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:02:51 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:02:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.110 |  |
| 2026-04-22 09:02:41 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-22 09:02:25 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-22 09:02:24 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.033 |  |
| 2026-04-22 09:02:24 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:02:07 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.022 |  |
| 2026-04-22 09:02:02 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:01:54 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.040 |  |
| 2026-04-22 09:01:45 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-22 09:01:41 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:01:38 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.030 |  |
| 2026-04-22 09:01:24 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2026-04-22 09:01:11 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-04-22 09:01:04 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:00:18 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 09:02:25 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-22 09:01:45 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-22 09:02:32 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-22 09:06:25 | Moragaswewa (Deduru Oya) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 09:01:41 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:03:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:03:16 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:03:52 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:02:02 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:10:10 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-22 09:10:08 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.009 |  |
| 2026-04-22 09:06:51 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-04-22 09:07:16 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-04-22 09:06:18 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:02:24 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:01:04 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:05:00 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:06:49 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-22 09:05:08 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-04-22 09:01:11 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.012 |  |
| 2026-04-22 09:12:00 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.018 |  |
| 2026-04-22 09:02:51 | Thanamalwila (Kirindi Oya) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:05:07 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:00:18 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:03:13 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-22 09:02:07 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.022 |  |
| 2026-04-22 09:01:38 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.030 |  |
| 2026-04-22 09:03:20 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.032 |  |
| 2026-04-22 09:02:24 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.033 |  |
| 2026-04-22 09:01:54 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | -0.040 |  |
| 2026-04-22 09:01:24 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.041 |  |
| 2026-04-22 09:06:36 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.043 |  |
| 2026-04-22 09:03:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.044 |  |
| 2026-04-22 08:12:16 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-04-22 09:05:34 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.058 |  |
| 2026-04-22 09:02:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.110 |  |
| 2026-04-22 09:05:31 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)