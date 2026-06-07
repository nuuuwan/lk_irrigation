# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_23:26:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 23:26:42 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:09:13 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:08:13 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-07 23:07:49 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:07:38 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.039 |  |
| 2026-06-07 23:07:38 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:07:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:06:57 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:06:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.085 |  |
| 2026-06-07 23:06:05 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:05:51 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.103 |  |
| 2026-06-07 23:05:48 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 23:05:36 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.020 |  |
| 2026-06-07 23:05:16 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-06-07 23:04:14 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-07 23:04:12 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 23:04:11 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:04:00 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.053 |  |
| 2026-06-07 23:03:45 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:03:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:03:25 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:45 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:45 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 23:02:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:20 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-06-07 23:02:15 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.040 |  |
| 2026-06-07 23:02:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 23:02:07 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 23:01:58 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:37 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-06-07 23:01:26 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:15 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.012 |  |
| 2026-06-07 23:01:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-07 23:00:54 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 23:04:14 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-07 23:08:13 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-07 23:05:48 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 23:04:12 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 23:02:07 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-07 22:17:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-07 23:02:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 23:02:45 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 23:06:05 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-06-07 22:03:27 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:58 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:45 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:03:25 | Deraniyagala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:09 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:42 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:03:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:26:42 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:26 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:07:20 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:07:49 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:03:45 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:09:13 | Thawalama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:02:41 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:06:57 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-07 23:01:08 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-07 23:01:15 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.012 |  |
| 2026-06-07 23:05:16 | Putupaula (Kalu Ganga) | 1.82 | 🟢 Normal | -0.019 |  |
| 2026-06-07 23:01:37 | Nawalapitiya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-06-07 23:05:36 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.020 |  |
| 2026-06-07 23:02:20 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-06-07 23:07:38 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.039 |  |
| 2026-06-07 23:02:15 | Hanwella (Kelani Ganga) | 3.86 | 🟢 Normal | -0.040 |  |
| 2026-06-07 23:04:00 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.053 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-07 23:06:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.085 |  |
| 2026-06-07 23:05:51 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)