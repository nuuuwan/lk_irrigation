# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--26_17:33:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **216,915 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 17:33:18 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:18:29 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:14:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:14:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:10:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-26 17:10:04 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.054 |  |
| 2026-07-26 17:08:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.084 |  |
| 2026-07-26 17:08:14 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.039 |  |
| 2026-07-26 17:08:06 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-26 17:08:01 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-26 17:07:40 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-26 17:07:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:06:45 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:06:22 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:05:25 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:05:13 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.023 |  |
| 2026-07-26 17:04:13 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:45 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:32 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:28 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-26 17:02:33 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-07-26 17:02:26 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:15 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-26 17:02:13 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:11 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:10 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:06 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-07-26 17:01:42 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:33 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:28 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:03 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:02 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 17:01:00 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -4.000 |  |
| 2026-07-26 17:00:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-07-26 17:00:16 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:00:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -4.000 |  |
| 2026-07-26 17:00:12 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-26 17:07:40 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-07-26 17:08:01 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-07-26 17:08:06 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-07-26 17:02:15 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-26 17:10:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-07-26 17:01:02 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-26 17:01:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:03 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:42 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:33 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:04:13 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:18:29 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:10 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:06:45 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:32 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:28 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:26 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:14:44 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:06:22 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:45 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:00:16 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:28 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:11 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:01:36 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:02:13 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:33:18 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:05:25 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:07:21 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:14:16 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-26 17:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-07-26 17:02:33 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-07-26 17:00:12 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-07-26 17:02:06 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-07-26 17:00:20 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-07-26 17:05:13 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.023 |  |
| 2026-07-26 17:08:14 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.039 |  |
| 2026-07-26 17:10:04 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.054 |  |
| 2026-07-26 17:08:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.084 |  |
| 2026-07-26 17:01:00 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -4.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)