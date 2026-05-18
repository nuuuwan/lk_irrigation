# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--18_21:11:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,523 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 21:11:26 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.018 |  |
| 2026-05-18 21:07:34 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-18 21:06:41 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-05-18 21:06:40 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:06:06 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-18 21:05:53 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:05:43 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:05:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:05:12 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-05-18 21:04:58 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:04:58 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.061 |  |
| 2026-05-18 21:03:52 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.097 |  |
| 2026-05-18 21:03:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-05-18 21:03:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:03:25 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 21:03:23 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.013 |  |
| 2026-05-18 21:03:16 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:03:00 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:02:50 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:02:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:02:41 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 21:02:34 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:02:31 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.178 |  |
| 2026-05-18 21:02:18 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.023 |  |
| 2026-05-18 21:02:11 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:57 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:50 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:44 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:30 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:01:01 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:00:49 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.022 |  |
| 2026-05-18 21:00:48 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:00:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 20:58:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-18 21:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-05-18 21:03:25 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-18 21:07:34 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-18 21:06:06 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-18 21:02:41 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-18 18:01:40 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:00:23 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:01:01 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:05:43 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-18 18:51:29 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:03:47 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:00:48 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:02:34 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:01:30 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:03:16 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:05:53 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:02:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:03:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:04:58 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-18 21:05:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:06:40 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:02:50 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:57 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:03:00 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:02:11 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:44 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:01:50 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-05-18 21:03:23 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.013 |  |
| 2026-05-18 21:11:26 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.018 |  |
| 2026-05-18 21:05:12 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-05-18 21:00:49 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.022 |  |
| 2026-05-18 21:06:41 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-05-18 21:02:18 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.023 |  |
| 2026-05-18 18:01:53 | Galgamuwa (Mee Oya) | 1.67 | 🟢 Normal | -0.033 |  |
| 2026-05-18 21:04:58 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | -0.061 |  |
| 2026-05-18 18:01:24 | Thanthirimale (Malwathu Oya) | 2.75 | 🟢 Normal | -0.082 |  |
| 2026-05-18 21:03:52 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.097 |  |
| 2026-05-18 21:02:31 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)