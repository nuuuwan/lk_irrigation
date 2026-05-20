# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--20_13:18:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **156,992 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 13:18:28 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:12:26 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.027 |  |
| 2026-05-20 13:10:38 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:09:53 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:09:42 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.046 |  |
| 2026-05-20 13:07:54 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:06:08 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:06:04 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-20 13:05:53 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 13:05:30 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-20 13:05:24 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-05-20 13:05:14 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-20 13:04:04 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:04:03 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-20 13:04:02 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-20 13:03:57 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:03:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 13:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:03:32 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:03:17 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-05-20 13:03:13 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:03:05 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:44 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:43 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:33 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.051 |  |
| 2026-05-20 13:02:21 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:17 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:02:17 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:16 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:02:05 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:18 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-05-20 13:01:08 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:00:38 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 12:59:50 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:59:43 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-20 13:04:03 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-05-20 13:06:04 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-20 13:05:30 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-20 13:00:38 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-20 13:03:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 13:05:53 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-20 13:03:13 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:08 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:03:05 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:03:32 | Giriulla (Maha Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:44 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:10:38 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:21 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:59:50 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:07:54 | Ellagawa (Kalu Ganga) | 5.23 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:03:39 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:05 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:17 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:18 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:01:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:18:28 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:02:43 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:04:04 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:03:57 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:06:08 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-20 12:00:49 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-05-20 13:09:53 | Holombuwa (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:02:17 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.21 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:02:16 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-20 13:05:24 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.011 |  |
| 2026-05-20 13:01:12 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-05-20 13:05:14 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-05-20 13:12:26 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.027 |  |
| 2026-05-20 13:03:17 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-05-20 13:09:42 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.046 |  |
| 2026-05-20 13:02:33 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)