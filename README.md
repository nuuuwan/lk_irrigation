# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_02:22:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,679 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 02:22:35 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-05-19 02:14:43 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-19 02:14:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.52 | 🟢 Normal | -0.053 |  |
| 2026-05-19 02:08:55 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-19 02:06:30 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.005 |  |
| 2026-05-19 02:06:15 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-05-19 02:05:58 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-05-19 02:05:31 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 1.272 | 🔺 Rising |
| 2026-05-19 02:05:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.028 |  |
| 2026-05-19 02:04:31 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.052 |  |
| 2026-05-19 02:04:22 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:04:10 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:03:42 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:03:27 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:03:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-19 02:03:19 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-19 02:03:04 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:02:58 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 02:02:37 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.029 |  |
| 2026-05-19 02:02:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:01:32 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:01:25 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 1.385 | 🔺 Rising |
| 2026-05-19 02:01:21 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 02:00:16 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 3.035 | 🔺 Rising |
| 2026-05-19 01:59:15 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 1.385 | 🔺 Rising |
| 2026-05-19 01:41:32 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.052 |  |
| 2026-05-19 01:40:30 | Wellawaya (Kirindi Oya) | 0.10 | 🟢 Normal | 3.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 02:00:16 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 3.035 | 🔺 Rising |
| 2026-05-19 02:01:25 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 1.385 | 🔺 Rising |
| 2026-05-19 02:05:31 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | 1.272 | 🔺 Rising |
| 2026-05-19 02:22:35 | Moraketiya (Walawe Ganga) | 1.98 | 🟢 Normal | 0.427 | 🔺 Rising |
| 2026-05-19 02:03:27 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-05-19 02:01:21 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-19 02:02:58 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-19 02:14:43 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-19 01:03:59 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:04:10 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 01:04:52 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:04:22 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:03:27 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-05-19 00:07:26 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:03:04 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:02:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:03:42 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:01:32 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 01:02:15 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-19 02:06:30 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.005 |  |
| 2026-05-19 00:14:04 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-05-19 01:05:26 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:05:07 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2026-05-19 02:08:55 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-05-19 02:03:19 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-05-18 23:20:37 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | -0.016 |  |
| 2026-05-19 01:03:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.022 |  |
| 2026-05-19 02:05:02 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.028 |  |
| 2026-05-19 02:02:37 | Ellagawa (Kalu Ganga) | 5.66 | 🟢 Normal | -0.029 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-19 02:06:15 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.040 |  |
| 2026-05-19 02:05:58 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.047 |  |
| 2026-05-19 01:02:28 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | -0.050 |  |
| 2026-05-19 02:04:31 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.052 |  |
| 2026-05-19 02:14:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.52 | 🟢 Normal | -0.053 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-19 01:00:24 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.087 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)