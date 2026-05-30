# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_15:20:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 15:20:31 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.028 |  |
| 2026-05-30 15:14:45 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.034 |  |
| 2026-05-30 15:13:35 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:13:21 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.071 |  |
| 2026-05-30 15:08:02 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:06:14 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-05-30 15:05:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -18.000 |  |
| 2026-05-30 15:05:52 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -18.000 |  |
| 2026-05-30 15:05:44 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:05:12 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:05:01 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:04:51 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 15:04:38 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 15:04:08 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:04:06 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | -0.068 |  |
| 2026-05-30 15:04:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:03:35 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.062 |  |
| 2026-05-30 15:03:14 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-30 15:03:08 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:03:07 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-30 15:02:56 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:02:55 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:02:49 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.111 |  |
| 2026-05-30 15:02:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:02:47 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | -0.044 |  |
| 2026-05-30 15:02:45 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:02:45 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-30 15:02:12 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:02:08 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.013 |  |
| 2026-05-30 15:01:57 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:01:33 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:01:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:16 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:12 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.31 | 🟡 Alert | -0.071 |  |
| 2026-05-30 15:00:52 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:00:37 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:00:36 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:00:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 15:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.31 | 🟡 Alert | -0.071 |  |
| 2026-05-30 15:03:14 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-05-30 15:04:38 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 15:04:51 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 15:08:02 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:02:55 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:02:47 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:04:03 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:32 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:05:01 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:00:37 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:05:12 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:03:08 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-30 14:00:56 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:16 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:00:36 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:13:35 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:33 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:02:45 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 15:01:12 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:01:57 | Putupaula (Kalu Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:02:12 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:00:36 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:04:08 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:02:56 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:05:44 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-05-30 15:02:08 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.013 |  |
| 2026-05-30 15:02:45 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-05-30 15:20:31 | Panadugama (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.028 |  |
| 2026-05-30 15:06:14 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-05-30 15:14:45 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.034 |  |
| 2026-05-30 15:02:47 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | -0.044 |  |
| 2026-05-30 15:03:35 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | -0.062 |  |
| 2026-05-30 15:04:06 | Ellagawa (Kalu Ganga) | 7.53 | 🟢 Normal | -0.068 |  |
| 2026-05-30 15:13:21 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.071 |  |
| 2026-05-30 15:02:49 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.111 |  |
| 2026-05-30 15:05:54 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)