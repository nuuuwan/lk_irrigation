# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_09:14:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 09:14:47 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:11:57 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-01-11 09:09:54 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:08:11 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-01-11 09:07:06 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.046 |  |
| 2026-01-11 09:06:56 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:05:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.103 |  |
| 2026-01-11 09:05:28 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:05:16 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:05:04 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:04:51 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:04:34 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:04:18 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:04:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.061 |  |
| 2026-01-11 09:03:54 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:03:22 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:03:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:03:18 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:03:02 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:02:58 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:02:48 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:02:41 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:02:18 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 09:02:17 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 09:02:07 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:02:05 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:01:57 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-01-11 09:01:53 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:48 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:48 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.065 |  |
| 2026-01-11 09:01:46 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:40 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-11 09:01:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:23 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:01:18 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:07 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-11 09:00:55 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:00:29 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:00:21 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 09:01:40 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-11 09:01:07 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-11 09:02:17 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-11 09:02:18 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 09:01:53 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:48 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:00:55 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:05:16 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:05:28 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:06:56 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:03:02 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:14:47 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:04:34 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:02:41 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:28 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:02:07 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:03:54 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:00:21 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:00:29 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:01:46 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:09:54 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:04:18 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:03:21 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:05:04 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-11 09:11:57 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.009 |  |
| 2026-01-11 09:02:48 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:03:18 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:01:23 | Horowpothana (Yan Oya) | 2.58 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:01:18 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:04:51 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:03:22 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:02:05 | Thaldena (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-11 09:08:11 | Padiyathalawa (Maduru Oya) | 1.12 | 🟢 Normal | -0.018 |  |
| 2026-01-11 09:01:57 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-01-11 09:07:06 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.046 |  |
| 2026-01-11 09:04:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.061 |  |
| 2026-01-11 09:01:48 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.065 |  |
| 2026-01-11 09:05:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)