# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_16:06:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,842 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 16:06:57 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:06:54 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-30 16:06:28 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.048 |  |
| 2026-05-30 16:05:35 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:04:58 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.135 |  |
| 2026-05-30 16:04:53 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:04:34 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:04:28 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.039 |  |
| 2026-05-30 16:04:20 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-30 16:04:17 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:03:54 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-30 16:03:41 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-05-30 16:03:13 | Ellagawa (Kalu Ganga) | 7.43 | 🟢 Normal | -0.101 |  |
| 2026-05-30 16:03:06 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:54 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:50 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-30 16:02:30 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-05-30 16:02:10 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-30 16:02:08 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:07 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.040 |  |
| 2026-05-30 16:02:04 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:56 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:51 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.27 | 🟡 Alert | -0.040 |  |
| 2026-05-30 16:01:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:00 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-30 16:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:00:49 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.044 |  |
| 2026-05-30 16:00:43 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-30 16:00:25 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.097 |  |
| 2026-05-30 16:00:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:59:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-30 15:20:31 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 16:01:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.27 | 🟡 Alert | -0.040 |  |
| 2026-05-30 16:06:54 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-30 16:04:20 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-30 15:59:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-30 16:04:53 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:03:06 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:00:11 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:04:17 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:00:37 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:04:34 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:06:57 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:08 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:04 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:54 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:05:35 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:13:35 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:56 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:01:51 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 16:02:50 | Dunamale (Aththanagalu Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:04:08 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-05-30 16:03:54 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-05-30 16:00:43 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:02:08 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.013 |  |
| 2026-05-30 16:03:41 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.019 |  |
| 2026-05-30 16:02:10 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-05-30 16:02:30 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-05-30 16:01:00 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.020 |  |
| 2026-05-30 15:20:31 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.028 |  |
| 2026-05-30 15:14:45 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.034 |  |
| 2026-05-30 16:04:28 | Hanwella (Kelani Ganga) | 2.80 | 🟢 Normal | -0.039 |  |
| 2026-05-30 16:02:07 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.040 |  |
| 2026-05-30 16:00:49 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.044 |  |
| 2026-05-30 16:06:28 | Rathnapura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.048 |  |
| 2026-05-30 16:00:25 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.097 |  |
| 2026-05-30 16:03:13 | Ellagawa (Kalu Ganga) | 7.43 | 🟢 Normal | -0.101 |  |
| 2026-05-30 16:04:58 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.135 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)