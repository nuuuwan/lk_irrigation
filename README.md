# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_07:14:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,370 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **47** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 07:14:15 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:14:09 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:14:02 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:13:56 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:13:51 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:13:45 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:13:38 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:13:35 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:13:29 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:11:46 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:11:22 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-05-14 07:10:18 | Rathnapura (Kalu Ganga) | 4.47 | 🟢 Normal | -0.155 |  |
| 2026-05-14 07:09:28 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.036 |  |
| 2026-05-14 07:09:11 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.018 |  |
| 2026-05-14 07:07:20 | Galgamuwa (Mee Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:07:07 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:07:01 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-14 07:06:38 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-14 07:06:04 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.250 |  |
| 2026-05-14 07:05:58 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:05:36 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.179 |  |
| 2026-05-14 07:05:36 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.133 |  |
| 2026-05-14 07:04:57 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.331 |  |
| 2026-05-14 07:04:56 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.075 |  |
| 2026-05-14 07:04:42 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:04:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.186 |  |
| 2026-05-14 07:04:22 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:04:20 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:04:01 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.113 |  |
| 2026-05-14 07:03:54 | Moragaswewa (Deduru Oya) | 1.60 | 🟢 Normal | -0.078 |  |
| 2026-05-14 07:03:51 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-14 07:03:13 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.031 |  |
| 2026-05-14 07:03:07 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:02:58 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.004 |  |
| 2026-05-14 07:02:46 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-14 07:02:43 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-05-14 07:02:25 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.039 |  |
| 2026-05-14 07:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-05-14 07:02:07 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-05-14 07:01:58 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:01:38 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 07:01:31 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:01:22 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-05-14 07:01:16 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.059 |  |
| 2026-05-14 07:01:01 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.032 |  |
| 2026-05-14 07:00:56 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.043 |  |
| 2026-05-14 07:00:39 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 07:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-05-14 07:06:04 | Magura (Kalu Ganga) | 4.31 | 🟡 Alert | -0.250 |  |
| 2026-05-14 07:02:43 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-05-14 07:07:01 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-14 07:06:38 | Badalgama (Maha Oya) | 3.02 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-14 07:01:38 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-14 07:03:07 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:07:20 | Galgamuwa (Mee Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:04:22 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:04:42 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:05:58 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:01:31 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:11:46 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:14:15 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:01:58 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:07:07 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:04:20 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-14 07:02:58 | Thanthirimale (Malwathu Oya) | 3.30 | 🟢 Normal | -0.004 |  |
| 2026-05-14 07:11:22 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.008 |  |
| 2026-05-14 07:03:51 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-05-14 07:02:46 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-05-14 07:09:11 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.018 |  |
| 2026-05-14 07:02:07 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-05-14 07:01:22 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-05-14 07:03:13 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.031 |  |
| 2026-05-14 07:01:01 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.032 |  |
| 2026-05-14 07:09:28 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.036 |  |
| 2026-05-14 07:02:25 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.039 |  |
| 2026-05-14 07:00:39 | Moraketiya (Walawe Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-05-14 07:00:56 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.043 |  |
| 2026-05-14 07:01:16 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.059 |  |
| 2026-05-14 07:04:56 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.075 |  |
| 2026-05-14 07:03:54 | Moragaswewa (Deduru Oya) | 1.60 | 🟢 Normal | -0.078 |  |
| 2026-05-14 07:04:01 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.113 |  |
| 2026-05-14 07:05:36 | Dunamale (Aththanagalu Oya) | 3.14 | 🟢 Normal | -0.133 |  |
| 2026-05-14 07:10:18 | Rathnapura (Kalu Ganga) | 4.47 | 🟢 Normal | -0.155 |  |
| 2026-05-14 07:05:36 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.179 |  |
| 2026-05-14 07:04:23 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.186 |  |
| 2026-05-14 07:04:57 | Kithulgala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.331 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)