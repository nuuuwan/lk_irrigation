# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--06_18:10:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,225 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 18:10:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:10:00 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 18:08:05 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:55 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-06-06 18:06:43 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:33 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:16 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.074 |  |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:01 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-06-06 18:04:54 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:04:27 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-06-06 18:04:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 18:04:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:04:22 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:04:11 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.049 |  |
| 2026-06-06 18:03:36 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:03:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:03:20 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2026-06-06 18:03:13 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-06-06 18:03:04 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-06-06 18:02:38 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.020 |  |
| 2026-06-06 18:02:16 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | -0.050 |  |
| 2026-06-06 18:02:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.063 |  |
| 2026-06-06 18:01:47 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-06-06 18:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:38 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-06 18:01:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.195 |  |
| 2026-06-06 18:01:30 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:03 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-06 18:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.021 |  |
| 2026-06-06 18:00:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:00:17 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-06 18:06:55 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-06-06 17:08:36 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-06 17:13:46 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-06-06 18:01:38 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-06-06 17:07:03 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-06-06 18:04:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-06 18:01:03 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-06 18:10:00 | Panadugama (Nilwala Ganga) | 2.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-06 18:06:04 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:33 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:00:17 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:45 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:10:22 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:07 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:04:54 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:04:22 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:38 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:43 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:00:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:02:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:03:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:43 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:01:30 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:08:05 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:03:36 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-06 18:06:01 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-06-06 17:03:01 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-06 18:04:27 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-06-06 18:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.17 | 🟢 Normal | -0.020 |  |
| 2026-06-06 18:01:47 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-06-06 18:00:31 | Nawalapitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.021 |  |
| 2026-06-06 18:03:13 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.030 |  |
| 2026-06-06 18:03:20 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.040 |  |
| 2026-06-06 18:03:04 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-06-06 18:04:11 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.049 |  |
| 2026-06-06 18:02:16 | Dunamale (Aththanagalu Oya) | 2.97 | 🟢 Normal | -0.050 |  |
| 2026-06-06 18:01:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.063 |  |
| 2026-06-06 18:06:16 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.074 |  |
| 2026-06-06 18:01:31 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)