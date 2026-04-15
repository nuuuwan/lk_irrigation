# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_20:23:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,024 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 20:23:36 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:23:14 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:09:17 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:07:37 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-04-15 20:07:10 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:07:06 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-15 20:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 20:06:21 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-04-15 20:06:00 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:05:59 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-15 20:05:54 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:05:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-04-15 20:05:31 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:04:42 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-04-15 20:04:34 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:04:10 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-15 20:04:10 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-15 20:04:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 20:04:06 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.050 |  |
| 2026-04-15 20:04:00 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:48 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:46 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 20:04:42 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-04-15 20:01:06 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-04-15 20:04:10 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-15 20:05:59 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-15 20:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-15 20:03:48 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:05:54 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:01:19 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:24 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:06:00 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:20 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:07:10 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:00:08 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:02:14 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:04:00 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:05:31 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:00:49 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:09:17 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:23:36 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:03:08 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:02:11 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-15 20:06:21 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.009 |  |
| 2026-04-15 20:07:37 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-04-15 20:04:09 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-15 20:03:46 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-15 20:04:10 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-04-15 20:03:06 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-04-15 20:02:17 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-04-15 19:00:35 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-04-15 20:07:06 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-04-15 20:02:37 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.021 |  |
| 2026-04-15 20:05:35 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.028 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 20:04:06 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.050 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |
| 2026-04-15 20:03:32 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)