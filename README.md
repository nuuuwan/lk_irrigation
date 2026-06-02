# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_03:57:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,949 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 03:57:57 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-06-03 03:32:30 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:30:48 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-03 03:30:47 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-03 03:30:45 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-03 03:13:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:10:50 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:08:58 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:08:02 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-06-03 03:07:45 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-03 03:07:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-03 03:07:08 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:06:13 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-03 03:06:11 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-03 03:06:06 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.112 |  |
| 2026-06-03 03:05:58 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 03:30:48 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-06-03 03:06:13 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-06-03 02:01:01 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-03 03:05:16 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-03 02:02:35 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-03 03:07:26 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-03 03:02:30 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-03 03:07:45 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-03 02:11:30 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 03:08:58 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:00:15 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:13:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:32:30 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:05:58 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:01:51 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:03:17 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:00:12 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:13:22 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:04:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:03:03 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:02:10 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:01:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:02:56 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:04:27 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-03 02:04:52 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:10:50 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-03 03:03:12 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -0.005 |  |
| 2026-06-03 03:05:05 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-06-03 03:05:03 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-06-03 03:57:57 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-06-03 03:04:05 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-06-03 03:02:43 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-06-03 03:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.021 |  |
| 2026-06-03 03:08:02 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-06-03 03:03:31 | Rathnapura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.033 |  |
| 2026-06-03 03:06:06 | Peradeniya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)