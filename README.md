# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_06:31:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,687 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 06:31:32 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 06:17:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:09:48 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-13 06:09:33 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-04-13 06:08:03 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:07:50 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 06:07:08 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:06:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.043 |  |
| 2026-04-13 06:06:47 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 06:06:40 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.042 |  |
| 2026-04-13 06:05:43 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-13 06:05:39 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-13 06:05:28 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:05:23 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:04:20 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -72.000 |  |
| 2026-04-13 06:04:19 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -72.000 |  |
| 2026-04-13 06:04:09 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 1.987 | 🔺 Rising |
| 2026-04-13 06:03:55 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-13 06:03:24 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.138 |  |
| 2026-04-13 06:03:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.082 |  |
| 2026-04-13 06:02:58 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:50 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:39 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-13 06:02:36 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-13 06:02:35 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:22 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-04-13 06:02:12 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:11 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-13 06:01:52 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-13 06:01:50 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-04-13 06:01:33 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.051 |  |
| 2026-04-13 06:01:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:01:13 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-13 06:00:56 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 06:00:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:00:46 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.024 |  |
| 2026-04-13 06:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 06:00:28 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.088 |  |
| 2026-04-13 05:53:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | 1.987 | 🔺 Rising |
| 2026-04-13 05:52:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | 1.987 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 06:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | 1.987 | 🔺 Rising |
| 2026-04-13 06:01:52 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-13 06:03:55 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-04-13 06:02:39 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-13 06:02:36 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-13 06:05:43 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-13 06:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 06:01:13 | Moragaswewa (Deduru Oya) | 0.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-13 06:31:32 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-13 06:06:47 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-13 06:00:56 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-13 06:07:50 | Kithulgala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-13 06:17:29 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:04:09 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:07:08 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:58 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:50 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:00:47 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:56 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:05:23 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:05:28 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:02:12 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:08:03 | Rathnapura (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 18:02:49 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:01:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 06:09:48 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.009 |  |
| 2026-04-13 06:09:33 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-04-13 06:05:39 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-04-13 06:01:50 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-04-13 06:02:11 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-13 06:00:46 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.024 |  |
| 2026-04-13 06:02:22 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.040 |  |
| 2026-04-13 06:06:40 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.042 |  |
| 2026-04-13 06:06:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.043 |  |
| 2026-04-13 06:01:33 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.051 |  |
| 2026-04-13 06:03:06 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.082 |  |
| 2026-04-13 06:00:28 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | -0.088 |  |
| 2026-04-13 06:03:24 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.138 |  |
| 2026-04-13 06:04:20 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)