# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--11_00:15:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **148,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 00:15:53 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 00:14:40 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.025 |  |
| 2026-05-11 00:13:47 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.033 |  |
| 2026-05-11 00:13:16 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:12:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-05-11 00:10:54 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-05-11 00:08:01 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 00:07:37 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-11 00:07:23 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:07:17 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.231 |  |
| 2026-05-11 00:06:46 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-05-11 00:06:21 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:05:07 | Thanamalwila (Kirindi Oya) | 4.90 | 🟡 Alert | 0.581 | 🔺 Rising |
| 2026-05-11 00:05:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-11 00:04:46 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-05-11 00:04:14 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 00:03:57 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-11 00:03:03 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 00:02:59 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-11 00:02:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-11 00:02:23 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 00:02:21 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-05-11 00:02:16 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-05-11 00:02:10 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 00:02:03 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.471 |  |
| 2026-05-11 00:01:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 00:01:35 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:01:30 | Kuda Oya (Kirindi Oya) | 6.10 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-05-11 00:01:22 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 00:01:10 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:01:02 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 00:00:54 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.094 |  |
| 2026-05-11 00:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-11 00:00:20 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | -1.995 |  |
| 2026-05-11 00:00:16 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-11 00:05:07 | Thanamalwila (Kirindi Oya) | 4.90 | 🟡 Alert | 0.581 | 🔺 Rising |
| 2026-05-11 00:01:30 | Kuda Oya (Kirindi Oya) | 6.10 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-05-11 00:07:37 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-05-11 00:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-11 00:15:53 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 00:01:22 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-05-11 00:03:57 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-11 00:08:01 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-11 00:02:23 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-05-11 00:03:03 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-05-11 00:01:54 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-11 00:02:30 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-11 00:01:02 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 00:02:10 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-11 00:04:14 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-11 00:02:59 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 22:02:10 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:06:14 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:06:21 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:01:35 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:13:16 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:01:10 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:00:16 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:07:23 | Katharagama (Menik Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-10 18:01:26 | Thanthirimale (Malwathu Oya) | 2.99 | 🟢 Normal | 0.000 |  |
| 2026-05-11 00:10:54 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.009 |  |
| 2026-05-11 00:02:16 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-05-11 00:12:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.011 |  |
| 2026-05-11 00:06:46 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-05-11 00:04:46 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.019 |  |
| 2026-05-10 18:03:02 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | -0.020 |  |
| 2026-05-11 00:02:21 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-05-11 00:14:40 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.025 |  |
| 2026-05-11 00:05:02 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-11 00:13:47 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.033 |  |
| 2026-05-11 00:00:54 | Glencourse (Kelani Ganga) | 9.41 | 🟢 Normal | -0.094 |  |
| 2026-05-11 00:07:17 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.231 |  |
| 2026-05-11 00:02:03 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.471 |  |
| 2026-05-11 00:00:20 | Wellawaya (Kirindi Oya) | 2.00 | 🟢 Normal | -1.995 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)