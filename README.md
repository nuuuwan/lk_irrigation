# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_22:05:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 22:05:06 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:04:56 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-24 22:04:51 | Deraniyagala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.239 |  |
| 2026-05-24 22:04:39 | Putupaula (Kalu Ganga) | 3.26 | 🟡 Alert | -0.010 |  |
| 2026-05-24 22:03:56 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:03:52 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-05-24 22:03:36 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:03:26 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-05-24 22:02:39 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.080 |  |
| 2026-05-24 22:02:33 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-24 22:02:24 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 22:02:23 | Ellagawa (Kalu Ganga) | 9.44 | 🟢 Normal | -0.040 |  |
| 2026-05-24 22:02:07 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:02:05 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:01:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:52 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-05-24 22:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-24 22:01:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:28 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:23 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:21 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:19 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:45 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-05-24 22:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:10 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-05-24 21:36:36 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 21:14:57 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | 0.217 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 22:04:39 | Putupaula (Kalu Ganga) | 3.26 | 🟡 Alert | -0.010 |  |
| 2026-05-24 21:01:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.16 | 🟡 Alert | -0.020 |  |
| 2026-05-24 22:03:26 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-05-24 21:14:57 | Rathnapura (Kalu Ganga) | 5.08 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-05-24 22:04:56 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-24 21:03:24 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-24 22:02:33 | Hanwella (Kelani Ganga) | 3.90 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-24 22:02:24 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 18:00:57 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:42 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:03:56 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:49 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:29 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:50 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:23 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:02:07 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:00:10 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:21 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-24 21:02:54 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-05-24 21:10:04 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-24 21:09:33 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 18:00:42 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:19 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:01:28 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 22:05:06 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:02:05 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:03:36 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-05-24 21:04:44 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-24 22:00:45 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-05-24 22:03:52 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.019 |  |
| 2026-05-24 22:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-05-24 22:01:52 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-05-24 21:04:54 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.023 |  |
| 2026-05-24 22:02:23 | Ellagawa (Kalu Ganga) | 9.44 | 🟢 Normal | -0.040 |  |
| 2026-05-24 21:05:33 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.061 |  |
| 2026-05-24 22:02:39 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.080 |  |
| 2026-05-24 22:04:51 | Deraniyagala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.239 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)