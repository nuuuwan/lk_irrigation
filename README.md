# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_04:18:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 04:18:28 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.008 |  |
| 2026-06-07 04:11:52 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:10:59 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:09:53 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-06-07 04:09:36 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-06-07 04:07:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:07:27 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:06:47 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-06-07 04:06:44 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-07 04:06:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -2.160 |  |
| 2026-06-07 04:05:44 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 04:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.97 | 🟢 Normal | -2.160 |  |
| 2026-06-07 04:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-07 04:05:09 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.00 | 🟢 Normal | -2.160 |  |
| 2026-06-07 04:04:57 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:04:42 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-07 04:04:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | -2.160 |  |
| 2026-06-07 04:04:31 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 04:04:08 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.066 |  |
| 2026-06-07 04:04:07 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:04:02 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:03:45 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:03:23 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:03:18 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-06-07 04:02:55 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 04:02:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 04:02:45 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | -0.021 |  |
| 2026-06-07 04:02:41 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:01:53 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:12 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 03:07:15 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | 0.994 | 🔺 Rising |
| 2026-06-07 04:09:36 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-06-07 04:09:53 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-06-07 04:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-06-07 04:06:44 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-07 04:04:31 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-07 04:02:54 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-07 04:05:44 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 04:02:55 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-07 04:02:41 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:10:59 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:03:45 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 04:04:57 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:04:02 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:22 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:12 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:49 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:03:23 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-06-06 21:04:41 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:11:52 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:04:07 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:07:34 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:19:46 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:07:27 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:01:53 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 04:05:09 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:07:09 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 03:21:36 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.007 |  |
| 2026-06-07 04:18:28 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.008 |  |
| 2026-06-07 04:04:42 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-06-07 04:03:18 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-06-07 01:08:42 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-06-07 04:06:47 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-06-07 04:02:45 | Ellagawa (Kalu Ganga) | 7.02 | 🟢 Normal | -0.021 |  |
| 2026-06-07 04:04:08 | Putupaula (Kalu Ganga) | 1.49 | 🟢 Normal | -0.066 |  |
| 2026-06-07 04:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -2.160 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)