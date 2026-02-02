# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_06:20:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,194 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 06:20:05 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.031 |  |
| 2026-02-02 06:13:52 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-02 06:12:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-02 06:11:26 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.036 |  |
| 2026-02-02 06:10:04 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 06:09:45 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-02-02 06:09:24 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-02-02 06:08:07 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:07:22 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:07:17 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.213 |  |
| 2026-02-02 06:06:51 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:06:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-02-02 06:06:39 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-02 06:06:19 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-02 06:05:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:05:34 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-02-02 06:05:33 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:05:31 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:05:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:04:30 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-02-02 06:04:29 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:04:20 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-02 06:04:02 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-02 06:03:47 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.021 |  |
| 2026-02-02 06:03:46 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:03:46 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:02:43 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.097 |  |
| 2026-02-02 06:02:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:02:37 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 06:02:32 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:01:46 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.114 |  |
| 2026-02-02 06:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 06:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-02 06:00:17 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-02 06:00:17 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:00:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:51:13 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | -0.032 |  |
| 2026-02-02 05:44:08 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:35:57 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-02 05:35:33 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-02-02 05:31:39 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 06:06:19 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-02 06:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 06:06:39 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-02 06:00:17 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-02 06:02:37 | Dunamale (Aththanagalu Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 06:10:04 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-02 06:13:52 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-02 06:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-02 06:05:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:02:42 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:05:11 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:03:46 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:05:31 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:02:32 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:03:46 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:05:33 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:04:29 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:00:17 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:06:51 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:08:07 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 05:44:08 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:00:17 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:07:22 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 06:04:02 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-02 06:04:30 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.011 |  |
| 2026-02-02 06:09:24 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.018 |  |
| 2026-02-02 06:04:20 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2026-02-02 06:12:34 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-02-02 06:03:47 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.021 |  |
| 2026-02-02 06:05:34 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.029 |  |
| 2026-02-02 06:20:05 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.031 |  |
| 2026-02-02 06:09:45 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.032 |  |
| 2026-02-02 06:11:26 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | -0.036 |  |
| 2026-02-02 06:06:41 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-02-02 06:02:43 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.097 |  |
| 2026-02-02 06:01:46 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.114 |  |
| 2026-02-02 06:07:17 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.213 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)