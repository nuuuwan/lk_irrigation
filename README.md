# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_07:27:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 07:27:27 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.048 |  |
| 2026-05-25 07:14:15 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.005 |  |
| 2026-05-25 07:10:02 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | -0.018 |  |
| 2026-05-25 07:09:23 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-05-25 07:09:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:09:05 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.027 |  |
| 2026-05-25 07:08:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.018 |  |
| 2026-05-25 07:08:02 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-05-25 07:07:49 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:07:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-25 07:07:08 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:06:52 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-05-25 07:06:41 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:06:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:05:43 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:05:39 | Rathnapura (Kalu Ganga) | 4.68 | 🟢 Normal | -0.122 |  |
| 2026-05-25 07:04:50 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:04:19 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.118 |  |
| 2026-05-25 07:04:12 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-05-25 07:04:11 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:50 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-25 07:02:45 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:42 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.223 |  |
| 2026-05-25 07:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.65 | 🟡 Alert | -0.138 |  |
| 2026-05-25 07:02:29 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-05-25 07:02:19 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:00 | Ellagawa (Kalu Ganga) | 9.14 | 🟢 Normal | -0.040 |  |
| 2026-05-25 07:01:50 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:01:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 07:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:01:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:01:08 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-25 07:00:52 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.027 |  |
| 2026-05-25 07:00:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.042 |  |
| 2026-05-25 07:00:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:00:10 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 07:10:02 | Putupaula (Kalu Ganga) | 3.14 | 🟡 Alert | -0.018 |  |
| 2026-05-25 07:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.65 | 🟡 Alert | -0.138 |  |
| 2026-05-25 07:06:52 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-05-25 07:07:41 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-25 07:02:50 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-25 06:03:53 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 07:01:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 07:14:15 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.005 |  |
| 2026-05-25 07:01:50 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:00:24 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:01:23 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:19 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:01:09 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:00:10 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:06:41 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:05:43 | Hanwella (Kelani Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:04:11 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:06:36 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:07:49 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:04:50 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:45 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:09:22 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:07:08 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:02:17 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 07:08:02 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-05-25 07:01:08 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-25 07:08:32 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.018 |  |
| 2026-05-25 07:09:23 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.019 |  |
| 2026-05-25 07:00:52 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | -0.027 |  |
| 2026-05-25 07:09:05 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.027 |  |
| 2026-05-25 07:04:12 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-05-25 07:02:29 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-05-25 07:02:00 | Ellagawa (Kalu Ganga) | 9.14 | 🟢 Normal | -0.040 |  |
| 2026-05-25 07:00:42 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.042 |  |
| 2026-05-25 07:27:27 | Nawalapitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.048 |  |
| 2026-05-25 06:01:47 | Thalgahagoda (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.059 |  |
| 2026-05-25 07:04:19 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.118 |  |
| 2026-05-25 07:05:39 | Rathnapura (Kalu Ganga) | 4.68 | 🟢 Normal | -0.122 |  |
| 2026-05-25 07:02:42 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.223 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)