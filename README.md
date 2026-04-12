# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--12_09:13:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 09:13:31 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-04-12 09:11:21 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:09:30 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:08:28 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:08:22 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:07:19 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.046 |  |
| 2026-04-12 09:06:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:45 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:33 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:24 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:21 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:03 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:41 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.039 |  |
| 2026-04-12 09:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-12 09:04:29 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-04-12 09:04:28 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 09:04:19 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:02 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:03:53 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 09:03:41 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-12 09:03:25 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-12 09:03:19 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:56 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 09:02:52 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 09:02:46 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:38 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.222 |  |
| 2026-04-12 09:02:37 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-04-12 09:02:33 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-12 09:02:33 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:31 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:29 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:01:34 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.320 |  |
| 2026-04-12 09:01:10 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-04-12 09:01:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:01:07 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:01:06 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.023 |  |
| 2026-04-12 09:00:42 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-12 09:02:33 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-12 09:03:25 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-12 09:03:41 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-12 09:04:28 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-12 09:02:52 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-12 09:02:56 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 09:03:53 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-12 09:03:19 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:01:07 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:21 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:33 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:45 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:01:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:29 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:11:21 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:08:22 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:00:42 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:33 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:24 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:31 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:06:59 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:02:46 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:08:28 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:09:30 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:19 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:02 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-12 09:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-04-12 09:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-12 09:02:37 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.021 |  |
| 2026-04-12 09:01:06 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.023 |  |
| 2026-04-12 09:04:29 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-04-12 09:01:10 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-04-12 09:04:41 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.039 |  |
| 2026-04-12 09:07:19 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.046 |  |
| 2026-04-12 09:13:31 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-04-12 09:02:38 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.222 |  |
| 2026-04-12 09:01:34 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.320 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)