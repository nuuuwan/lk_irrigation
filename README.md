# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_12:08:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **164,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 12:08:07 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 12:07:54 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-29 12:07:26 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:07:22 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.040 |  |
| 2026-05-29 12:07:12 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.028 |  |
| 2026-05-29 12:06:36 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:06:35 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:06:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-29 12:06:21 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-05-29 12:05:18 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 12:04:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 12:04:19 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.033 |  |
| 2026-05-29 12:04:18 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-29 12:04:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.009 |  |
| 2026-05-29 12:03:42 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.063 |  |
| 2026-05-29 12:03:35 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:03:35 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:03:13 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:03:02 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.052 |  |
| 2026-05-29 12:02:56 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-05-29 12:02:54 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.063 |  |
| 2026-05-29 12:02:42 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-05-29 12:02:26 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:02:23 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:02:23 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.061 |  |
| 2026-05-29 12:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-05-29 12:02:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 12:02:13 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:01:34 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.075 |  |
| 2026-05-29 12:01:32 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:01:26 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-29 12:01:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:01:00 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 12:00:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:00:27 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:00:16 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 12:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.69 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-29 11:14:04 | Magura (Kalu Ganga) | 4.40 | 🟡 Alert | -0.019 |  |
| 2026-05-29 11:05:22 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-29 12:06:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-29 12:07:54 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-29 12:08:07 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-29 12:01:00 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-29 12:02:20 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 12:05:18 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 12:02:26 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:00:27 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:03:35 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:02:23 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:00:37 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:06:35 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:03:13 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:00:16 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:02:13 | Dunamale (Aththanagalu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:01:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:04:57 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:06:36 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:07:26 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:01:32 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:03:35 | Thalgahagoda (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 12:04:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.009 |  |
| 2026-05-29 12:04:18 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-05-29 12:01:26 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-05-29 12:02:56 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | -0.010 |  |
| 2026-05-29 12:02:42 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-05-29 12:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2026-05-29 12:07:12 | Glencourse (Kelani Ganga) | 11.50 | 🟢 Normal | -0.028 |  |
| 2026-05-29 12:06:21 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-05-29 12:04:19 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | -0.033 |  |
| 2026-05-29 12:07:22 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.040 |  |
| 2026-05-29 12:03:02 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.052 |  |
| 2026-05-29 12:02:23 | Deraniyagala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.061 |  |
| 2026-05-29 12:03:42 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.063 |  |
| 2026-05-29 12:02:54 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.063 |  |
| 2026-05-29 12:01:34 | Peradeniya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)