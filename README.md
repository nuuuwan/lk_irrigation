# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--28_10:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **163,831 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 10:12:00 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:11:35 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:10:42 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-05-28 10:06:24 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-05-28 10:06:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:05:38 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:05:32 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 10:05:26 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-28 10:05:22 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:04:55 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.070 |  |
| 2026-05-28 10:04:31 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-28 10:04:13 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.075 |  |
| 2026-05-28 10:04:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:03:52 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:03:24 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-28 10:03:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:03:12 | Rathnapura (Kalu Ganga) | 4.03 | 🟢 Normal | -0.103 |  |
| 2026-05-28 10:03:08 | Putupaula (Kalu Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.104 |  |
| 2026-05-28 10:02:54 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 10:02:40 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:31 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:02:23 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-28 10:02:22 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.071 |  |
| 2026-05-28 10:02:19 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-28 10:02:15 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:02:10 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.025 |  |
| 2026-05-28 10:02:09 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:09 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:07 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:01:48 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-28 10:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:00:49 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:00:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:00:36 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 10:00:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-28 10:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-05-28 10:03:24 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-28 10:00:36 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-28 10:02:23 | Baddegama (Gin Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-28 10:04:31 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-28 10:05:26 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-28 10:02:19 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 10:02:54 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-28 10:05:32 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-28 10:03:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:00:49 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:11:35 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:01:40 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:05:39 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:00:43 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:03:52 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:05:38 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-28 09:13:33 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:06:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:02:15 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:00:28 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:04:00 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:02:31 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-28 10:10:42 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-05-28 10:05:22 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:12:00 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:40 | Deraniyagala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:09 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:07 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:02:09 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:03:08 | Putupaula (Kalu Ganga) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-05-28 10:01:48 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-05-28 10:02:10 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | -0.025 |  |
| 2026-05-28 10:06:24 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-05-28 10:04:55 | Peradeniya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.070 |  |
| 2026-05-28 10:02:22 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.071 |  |
| 2026-05-28 10:04:13 | Glencourse (Kelani Ganga) | 11.68 | 🟢 Normal | -0.075 |  |
| 2026-05-28 10:03:12 | Rathnapura (Kalu Ganga) | 4.03 | 🟢 Normal | -0.103 |  |
| 2026-05-28 10:02:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)