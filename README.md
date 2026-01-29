# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_09:14:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,698 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 09:14:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:12:50 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:09:50 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-29 09:08:34 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.066 |  |
| 2026-01-29 09:08:11 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 09:07:48 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:07:09 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:06:13 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:05:59 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:05:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-29 09:05:52 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.019 |  |
| 2026-01-29 09:05:51 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:05:30 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:33 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:03 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:50 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:44 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:43 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-29 09:03:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:20 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-29 09:03:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:03 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 09:02:48 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-29 09:02:31 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-29 09:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.054 |  |
| 2026-01-29 09:02:01 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:49 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-01-29 09:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:31 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-29 09:01:27 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-29 09:01:26 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:25 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-29 09:01:22 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:44 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:09 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 09:02:48 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-29 09:01:31 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-29 09:03:20 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-29 09:03:03 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-29 09:03:43 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-29 09:05:55 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-29 09:08:11 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 09:03:17 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:33 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:18 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:44 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:00:09 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:50 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:07:09 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:02:01 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:12:50 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:05:59 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:42 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:03:44 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:22 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:04:03 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:05:51 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:06:13 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:07:48 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:38 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:14:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:26 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 09:01:25 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-01-29 09:09:50 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-29 09:02:31 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-01-29 09:05:52 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.019 |  |
| 2026-01-29 09:01:27 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.020 |  |
| 2026-01-29 08:00:35 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-01-29 09:01:49 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.040 |  |
| 2026-01-29 09:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.054 |  |
| 2026-01-29 09:08:34 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)