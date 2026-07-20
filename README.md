# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--20_09:14:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 09:14:50 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:13:37 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:13:28 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:12:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-20 09:11:25 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:10:01 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 09:08:36 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-20 09:07:18 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.119 |  |
| 2026-07-20 09:07:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:06:41 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:06:30 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:05:37 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 09:04:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 09:04:02 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.080 |  |
| 2026-07-20 09:03:27 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 09:03:24 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.071 |  |
| 2026-07-20 09:03:07 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-20 09:03:05 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:03:03 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:52 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:52 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:36 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-20 09:02:35 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:28 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:27 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.176 |  |
| 2026-07-20 09:02:21 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 09:02:12 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 09:01:51 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-07-20 09:01:46 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:01:39 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:00:49 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 09:00:34 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:00:17 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-20 09:01:51 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-07-20 09:02:36 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-20 09:03:07 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-07-20 09:00:49 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-20 09:12:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-20 09:02:12 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 09:10:01 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 09:05:37 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-20 09:03:27 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 09:02:21 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 09:04:25 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-20 09:02:52 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:00:17 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:03:03 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:00:24 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:01:39 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:03:05 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:00:34 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:36 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:13:37 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:06:30 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:14:50 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:13:28 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:42 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:03:24 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:35 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:06:41 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:01:46 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:02:28 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:07:09 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:11:25 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-20 08:03:16 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-20 09:08:36 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-07-20 08:03:07 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.012 |  |
| 2026-07-20 09:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.071 |  |
| 2026-07-20 09:04:02 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.080 |  |
| 2026-07-20 09:07:18 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.119 |  |
| 2026-07-20 09:02:27 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)