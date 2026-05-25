# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_09:11:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,117 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 09:11:01 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:09:27 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:08:23 | Glencourse (Kelani Ganga) | 12.39 | 🟢 Normal | -0.121 |  |
| 2026-05-25 09:08:04 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-25 09:07:56 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:07:35 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 09:06:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-25 09:06:51 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:06:46 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.019 |  |
| 2026-05-25 09:05:51 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-25 09:05:43 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-25 09:05:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:04:27 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-25 09:04:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:04:01 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:03:54 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.140 |  |
| 2026-05-25 09:03:48 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-25 09:03:43 | Ellagawa (Kalu Ganga) | 9.08 | 🟢 Normal | -0.020 |  |
| 2026-05-25 09:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.078 |  |
| 2026-05-25 09:03:31 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:03:15 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:03:10 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-25 09:03:05 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.058 |  |
| 2026-05-25 09:02:51 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 09:02:50 | Putupaula (Kalu Ganga) | 3.05 | 🟡 Alert | -0.039 |  |
| 2026-05-25 09:02:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 09:02:46 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-25 09:02:40 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | -0.051 |  |
| 2026-05-25 09:02:18 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:02:17 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.088 |  |
| 2026-05-25 09:02:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-05-25 09:01:41 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.021 |  |
| 2026-05-25 09:01:32 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:29 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:00:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:00:24 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 09:02:50 | Putupaula (Kalu Ganga) | 3.05 | 🟡 Alert | -0.039 |  |
| 2026-05-25 09:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.55 | 🟡 Alert | -0.051 |  |
| 2026-05-25 09:08:04 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-25 09:06:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-25 09:04:27 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-25 09:03:10 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-25 09:05:51 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-25 09:05:43 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-25 09:02:46 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 09:07:35 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 09:02:51 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 09:00:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:02:40 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:21 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:04:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:03:31 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:09:27 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:11:01 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:06:51 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:29 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:05:19 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:07:56 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:04:01 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:01:32 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:03:15 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:00:24 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:02:18 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 09:06:46 | Hanwella (Kelani Ganga) | 5.00 | 🟢 Normal | -0.019 |  |
| 2026-05-25 09:03:43 | Ellagawa (Kalu Ganga) | 9.08 | 🟢 Normal | -0.020 |  |
| 2026-05-25 09:02:46 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-25 09:03:48 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-25 09:01:41 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.021 |  |
| 2026-05-25 09:02:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |
| 2026-05-25 09:03:05 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.058 |  |
| 2026-05-25 09:03:39 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.078 |  |
| 2026-05-25 09:02:17 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.088 |  |
| 2026-05-25 09:08:23 | Glencourse (Kelani Ganga) | 12.39 | 🟢 Normal | -0.121 |  |
| 2026-05-25 09:03:54 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)