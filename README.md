# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--04_22:13:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **116,295 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 22:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-04-04 22:10:09 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:09:36 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.134 |  |
| 2026-04-04 22:08:49 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-04-04 22:08:00 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-04-04 22:07:44 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-04-04 22:07:08 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-04 22:06:49 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:05:59 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:05:49 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-04-04 22:05:33 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 22:05:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2026-04-04 22:05:12 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-04-04 22:04:48 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:04:48 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:04:13 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-04-04 22:04:09 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 22:03:50 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:03:30 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.117 |  |
| 2026-04-04 22:03:19 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 22:03:07 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:03:01 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.011 |  |
| 2026-04-04 22:02:54 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 22:02:52 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-04 22:02:35 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-04-04 22:02:30 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.031 |  |
| 2026-04-04 22:02:21 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-04 22:02:14 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-04-04 22:02:07 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:02:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 22:01:30 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 22:01:20 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:01:16 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.035 |  |
| 2026-04-04 22:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:00:08 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-04 22:02:35 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-04-04 22:01:30 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-04 22:02:04 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 22:02:54 | Manampitiya (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-04 22:05:33 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 22:03:19 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 22:04:09 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-04 22:00:08 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:10:09 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:05:59 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:00:23 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:01:20 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-04 17:58:33 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:06:49 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:03:50 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:04:48 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:03:07 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 21:03:37 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:04:48 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:02:07 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-04 22:07:44 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-04-04 22:08:00 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-04-04 22:07:08 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-04 22:02:52 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-04-04 22:02:21 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-04 22:03:01 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.011 |  |
| 2026-04-04 22:13:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-04-04 22:02:14 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-04-04 22:05:12 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.029 |  |
| 2026-04-04 22:04:13 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-04-04 18:01:01 | Thanthirimale (Malwathu Oya) | 2.52 | 🟢 Normal | -0.031 |  |
| 2026-04-04 22:02:30 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.031 |  |
| 2026-04-04 22:01:16 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.035 |  |
| 2026-04-04 22:05:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.039 |  |
| 2026-04-04 22:08:49 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-04-04 22:05:49 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.048 |  |
| 2026-04-04 18:01:27 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.050 |  |
| 2026-04-04 22:03:30 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.117 |  |
| 2026-04-04 22:09:36 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)