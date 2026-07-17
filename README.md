# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--17_20:54:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,965 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 20:54:22 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:26:10 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:19:08 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:12:57 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:09:36 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:08:49 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:07:41 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.286 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-17 20:07:41 | Peradeniya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-07-17 20:03:54 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-17 20:02:34 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-17 20:02:07 | Glencourse (Kelani Ganga) | 8.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-17 20:03:15 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:03:33 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:01:37 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:19:08 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:02:06 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:03:11 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:08:49 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:06:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:01:04 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:04:50 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:03:07 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:02:02 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:00:15 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:02:47 | Moraketiya (Walawe Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:01:59 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:54:22 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:00:31 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:03:45 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:12:57 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:03:48 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:04:34 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:09:36 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:26:10 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:01:11 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:04:48 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 20:06:17 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-07-17 20:04:31 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-07-17 20:02:12 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-07-17 20:06:53 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-07-17 20:04:57 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.012 |  |
| 2026-07-17 20:03:39 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.019 |  |
| 2026-07-17 20:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.029 |  |
| 2026-07-17 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-07-17 20:02:09 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.104 |  |
| 2026-07-17 20:02:45 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)