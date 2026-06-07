# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_13:20:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 13:20:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-06-07 13:18:23 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-07 13:09:25 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.044 |  |
| 2026-06-07 13:07:38 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 13:07:27 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.058 |  |
| 2026-06-07 13:06:32 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.019 |  |
| 2026-06-07 13:06:22 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 13:06:17 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 13:06:13 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:05:22 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:05:05 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.089 |  |
| 2026-06-07 13:04:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 13:04:14 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 13:04:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:03:33 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:03:30 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:03:26 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 13:03:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 13:03:16 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-07 13:03:00 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-07 13:02:58 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:54 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 13:02:54 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-07 13:02:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:51 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:43 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-07 13:02:43 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:36 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.030 |  |
| 2026-06-07 13:02:19 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-06-07 13:02:04 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 13:02:03 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:01 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:01:52 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:01:42 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:01:14 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-06-07 13:01:11 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-07 13:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-07 13:00:23 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:00:20 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 13:02:54 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-06-07 13:03:16 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-06-07 13:01:11 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-07 13:03:00 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-07 13:06:17 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 13:00:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-07 13:04:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 13:07:38 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-07 13:18:23 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-07 13:02:04 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 13:03:24 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 13:06:22 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 13:02:54 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 13:04:14 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 13:03:26 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 13:00:20 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:58 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:04:12 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:03:33 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:01 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:00:23 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:03:30 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:05:22 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:06:13 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:52 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:43 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:51 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:02:03 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:01:42 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:01:52 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:20:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-06-07 13:02:43 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-06-07 13:06:32 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.019 |  |
| 2026-06-07 13:01:14 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-06-07 13:02:19 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-06-07 13:02:36 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.030 |  |
| 2026-06-07 13:09:25 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.044 |  |
| 2026-06-07 13:07:27 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.058 |  |
| 2026-06-07 13:05:05 | Rathnapura (Kalu Ganga) | 4.52 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)