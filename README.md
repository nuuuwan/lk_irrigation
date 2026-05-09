# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_07:21:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 07:21:32 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:18:35 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.035 |  |
| 2026-05-09 07:17:57 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.032 |  |
| 2026-05-09 07:16:38 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-09 07:15:03 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-09 07:14:11 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.055 |  |
| 2026-05-09 07:13:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-09 07:12:49 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.092 |  |
| 2026-05-09 07:10:09 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-05-09 07:09:07 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:09:06 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.080 |  |
| 2026-05-09 07:08:47 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:07:55 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.081 |  |
| 2026-05-09 07:07:27 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.028 |  |
| 2026-05-09 07:06:31 | Galgamuwa (Mee Oya) | 2.88 | 🟢 Normal | -0.127 |  |
| 2026-05-09 07:05:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-05-09 07:05:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:05:50 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-09 07:05:44 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-09 07:05:34 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.063 |  |
| 2026-05-09 07:05:15 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 07:05:04 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:04:57 | Thanamalwila (Kirindi Oya) | 2.98 | 🟢 Normal | -0.557 |  |
| 2026-05-09 07:04:37 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:03:50 | Katharagama (Menik Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 07:03:03 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-05-09 07:02:57 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.095 |  |
| 2026-05-09 07:02:38 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-09 07:02:31 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:02:24 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.065 |  |
| 2026-05-09 07:02:04 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-09 07:01:49 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.041 |  |
| 2026-05-09 07:01:36 | Kuda Oya (Kirindi Oya) | 3.05 | 🟢 Normal | -0.646 |  |
| 2026-05-09 07:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-05-09 07:01:16 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:01:08 | Thanthirimale (Malwathu Oya) | 3.31 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-09 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-09 07:00:57 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:00:11 | Wellawaya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-05-09 06:33:27 | Galgamuwa (Mee Oya) | 2.95 | 🟢 Normal | -0.127 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 05:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-09 07:02:04 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-05-09 07:01:07 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-05-09 07:01:08 | Thanthirimale (Malwathu Oya) | 3.31 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-05-09 07:02:38 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-09 07:13:08 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-09 07:15:03 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-09 07:05:15 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-09 07:05:50 | Moragaswewa (Deduru Oya) | 3.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-09 07:16:38 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-09 07:03:50 | Katharagama (Menik Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 07:01:16 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:05:04 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:05:51 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:04:37 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:08:47 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:09:07 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:02:31 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:21:32 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 07:05:44 | Moraketiya (Walawe Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-09 07:03:03 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.021 |  |
| 2026-05-09 07:10:09 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.026 |  |
| 2026-05-09 07:07:27 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -0.028 |  |
| 2026-05-09 07:05:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-05-09 07:01:20 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.029 |  |
| 2026-05-09 07:17:57 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.032 |  |
| 2026-05-09 07:18:35 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.035 |  |
| 2026-05-09 07:01:49 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.041 |  |
| 2026-05-09 07:14:11 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.055 |  |
| 2026-05-09 07:05:34 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.063 |  |
| 2026-05-09 07:02:24 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.065 |  |
| 2026-05-09 07:00:11 | Wellawaya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.071 |  |
| 2026-05-09 07:09:06 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | -0.080 |  |
| 2026-05-09 07:07:55 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | -0.081 |  |
| 2026-05-09 07:12:49 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.092 |  |
| 2026-05-09 07:02:57 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.095 |  |
| 2026-05-09 07:06:31 | Galgamuwa (Mee Oya) | 2.88 | 🟢 Normal | -0.127 |  |
| 2026-05-09 07:04:57 | Thanamalwila (Kirindi Oya) | 2.98 | 🟢 Normal | -0.557 |  |
| 2026-05-09 07:01:36 | Kuda Oya (Kirindi Oya) | 3.05 | 🟢 Normal | -0.646 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)