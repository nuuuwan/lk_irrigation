# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--21_14:10:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **185,447 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 14:10:03 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:08:25 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:08:12 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.046 |  |
| 2026-06-21 14:08:07 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-06-21 14:07:37 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:07:24 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 14:06:43 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.038 |  |
| 2026-06-21 14:06:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.022 |  |
| 2026-06-21 14:05:42 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:05:18 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:05:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-21 14:04:29 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:36 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:25 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 14:03:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 14:03:06 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-21 14:03:05 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:03 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:59 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:37 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:35 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 14:02:34 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-21 14:02:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:09 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:03 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:01:59 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.383 |  |
| 2026-06-21 14:01:55 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-21 14:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-21 14:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:00:55 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-21 14:00:44 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-21 14:00:39 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:00:25 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.383 |  |
| 2026-06-21 14:00:06 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 13:21:48 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-21 14:02:34 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-06-21 14:05:13 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-21 14:01:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-06-21 13:17:26 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-06-21 14:07:24 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-21 13:07:11 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 14:03:25 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-21 13:15:26 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-06-21 14:00:55 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-21 14:03:15 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 14:02:35 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-21 14:00:39 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:00:06 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:03 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:01:20 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:03 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-06-21 13:03:39 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:05 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:10:03 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:36 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:08:25 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:03:18 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:07:37 | Dunamale (Aththanagalu Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:37 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:09 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:04:29 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:05:18 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-06-21 13:21:48 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:02:59 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-21 14:01:55 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-06-21 14:03:06 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-06-21 14:00:44 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-06-21 14:08:07 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-06-21 14:06:25 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.022 |  |
| 2026-06-21 14:06:43 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.038 |  |
| 2026-06-21 14:08:12 | Glencourse (Kelani Ganga) | 9.86 | 🟢 Normal | -0.046 |  |
| 2026-06-21 14:01:59 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.383 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)