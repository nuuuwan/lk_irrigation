# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--10_09:23:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **202,283 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 09:23:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:18:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.058 |  |
| 2026-07-10 09:14:37 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-07-10 09:11:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-10 09:09:06 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 09:08:40 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-10 09:08:37 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.051 |  |
| 2026-07-10 09:08:15 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:07:36 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:07:33 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:07:17 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:06:50 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:49 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:47 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-10 09:05:34 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-10 09:05:26 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:26 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:13 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:13 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:04:31 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.208 |  |
| 2026-07-10 09:04:26 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:04:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 09:03:48 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:03:28 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-07-10 09:03:09 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-07-10 09:02:54 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:54 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:16 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-10 09:02:14 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:14 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:01:41 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.032 |  |
| 2026-07-10 09:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.089 |  |
| 2026-07-10 09:01:10 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-10 09:01:05 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:01:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:58 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:57 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:49 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:10 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.046 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-10 09:03:09 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-07-10 09:14:37 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-07-10 09:01:10 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-10 09:00:10 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-07-10 09:05:34 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-07-10 09:05:43 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-10 09:11:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-10 09:02:16 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-10 09:08:40 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-10 09:04:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 09:09:06 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 09:07:17 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:08:15 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:01:05 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:03:48 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:13 | Yaka Wewa (Ma Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:13 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:49 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:06:50 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:47 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:14 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:23:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:07:36 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:54 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:14 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:26 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:52 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:04:26 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:02:54 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:58 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:01:05 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:00:57 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:05:26 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-10 09:03:28 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-07-10 09:01:41 | Thalgahagoda (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.032 |  |
| 2026-07-10 09:08:37 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | -0.051 |  |
| 2026-07-10 09:18:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.058 |  |
| 2026-07-10 09:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.089 |  |
| 2026-07-10 09:04:31 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.208 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)