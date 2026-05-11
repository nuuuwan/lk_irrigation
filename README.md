# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_02:40:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 02:40:54 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-05-12 02:40:03 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-05-12 02:16:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.085 |  |
| 2026-05-12 02:14:39 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-05-12 02:12:30 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-12 02:08:36 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.029 |  |
| 2026-05-12 02:08:07 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 02:07:38 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:06:58 | Katharagama (Menik Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-12 02:06:08 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:05:40 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 02:05:17 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 02:05:12 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-12 02:05:12 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-05-12 02:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:04:15 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:04:04 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -1.636 |  |
| 2026-05-12 02:04:02 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | -0.206 |  |
| 2026-05-12 02:03:59 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:03:52 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 00:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-05-11 18:01:53 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 02:01:45 | Ellagawa (Kalu Ganga) | 5.77 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-05-12 01:04:07 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 02:05:12 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-12 02:06:58 | Katharagama (Menik Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-12 02:12:30 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-12 01:18:23 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-12 02:02:45 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 02:05:17 | Magura (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 02:08:07 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 02:05:40 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-12 02:04:15 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:05:04 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:03:59 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:07:38 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 01:13:33 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:00:55 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:06:08 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-12 02:14:39 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-05-12 02:03:52 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.016 |  |
| 2026-05-12 02:40:03 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-05-12 02:05:12 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-05-12 02:40:54 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-05-12 02:02:25 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-05-12 02:08:36 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.029 |  |
| 2026-05-12 02:01:26 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.030 |  |
| 2026-05-11 18:02:56 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.049 |  |
| 2026-05-12 02:02:28 | Thanamalwila (Kirindi Oya) | 2.27 | 🟢 Normal | -0.050 |  |
| 2026-05-12 02:02:53 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.053 |  |
| 2026-05-12 02:02:49 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | -0.062 |  |
| 2026-05-12 02:02:12 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.064 |  |
| 2026-05-11 18:06:15 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.074 |  |
| 2026-05-12 02:16:28 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.085 |  |
| 2026-05-12 02:01:46 | Kuda Oya (Kirindi Oya) | 2.39 | 🟢 Normal | -0.101 |  |
| 2026-05-12 02:02:21 | Siyambalanduwa (Heda Oya) | 1.38 | 🟢 Normal | -0.185 |  |
| 2026-05-12 02:04:02 | Moragaswewa (Deduru Oya) | 2.45 | 🟢 Normal | -0.206 |  |
| 2026-05-12 02:04:04 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -1.636 |  |
| 2026-05-12 02:02:50 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -4.500 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)