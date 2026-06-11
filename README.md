# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--11_20:16:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **176,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 20:16:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-11 20:14:19 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:14:13 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-06-11 20:13:16 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 20:12:47 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 20:12:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-06-11 20:10:33 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.977 | 🔺 Rising |
| 2026-06-11 20:07:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:07:31 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 20:06:45 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 20:06:44 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-11 20:05:36 | Deraniyagala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-06-11 20:05:28 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:05:24 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-06-11 20:05:23 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-11 20:05:20 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-06-11 20:04:53 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-11 20:04:51 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:04:34 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 20:03:53 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.050 |  |
| 2026-06-11 20:03:53 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:03:50 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-11 20:03:49 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-06-11 20:03:31 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:03:09 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 20:02:52 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 20:02:43 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:02:35 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:02:21 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-11 20:02:16 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-11 20:02:16 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2026-06-11 20:01:48 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-11 20:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:01:40 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 20:01:18 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:01:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-11 20:10:33 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.977 | 🔺 Rising |
| 2026-06-11 20:05:36 | Deraniyagala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-06-11 20:05:24 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-06-11 20:04:53 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-06-11 20:03:49 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-06-11 20:02:16 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-11 20:03:50 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-11 20:02:21 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-11 20:05:23 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-06-11 20:06:44 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-11 20:02:52 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-06-11 20:01:48 | Thawalama (Gin Ganga) | 2.37 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-11 20:12:47 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-06-11 20:16:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-11 20:03:09 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-11 20:04:34 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 20:13:16 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-11 20:01:40 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 20:06:45 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 20:07:31 | Panadugama (Nilwala Ganga) | 3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-11 20:02:35 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:02:43 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:03:53 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:01:41 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:14:19 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:01:18 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:05:28 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:01:18 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:07:58 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:04:51 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:03:31 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-11 20:14:13 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-11 20:12:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.028 |  |
| 2026-06-11 20:02:16 | Nawalapitiya (Mahaweli Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2026-06-11 20:05:20 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.031 |  |
| 2026-06-11 20:03:53 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)