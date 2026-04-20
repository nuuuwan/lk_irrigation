# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_03:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 03:03:00 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-04-21 03:02:53 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.049 |  |
| 2026-04-21 03:02:53 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 03:02:34 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:02:32 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 03:02:32 | Thanamalwila (Kirindi Oya) | 4.27 | 🟡 Alert | -0.101 |  |
| 2026-04-21 03:02:24 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-04-21 03:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:01:10 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:48:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-04-21 02:25:54 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 02:22:14 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-21 02:22:05 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 02:21:19 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.124 |  |
| 2026-04-21 02:15:51 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.058 |  |
| 2026-04-21 02:12:28 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:11:43 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.216 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 03:02:32 | Thanamalwila (Kirindi Oya) | 4.27 | 🟡 Alert | -0.101 |  |
| 2026-04-21 02:03:22 | Kuda Oya (Kirindi Oya) | 4.18 | 🟢 Normal | 26.349 | 🔺 Rising |
| 2026-04-21 02:06:59 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.467 | 🔺 Rising |
| 2026-04-21 02:48:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | 0.345 | 🔺 Rising |
| 2026-04-21 02:02:37 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-04-21 03:03:00 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 02:03:44 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 01:03:25 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-04-21 02:09:28 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-21 02:02:44 | Dunamale (Aththanagalu Oya) | 0.75 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-21 01:03:54 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-21 02:00:32 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 02:22:05 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-21 03:02:53 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-21 02:01:01 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 02:02:50 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 02:22:14 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-21 03:02:32 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 01:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 03:02:34 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:01:17 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:01:53 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:01:35 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-20 23:02:37 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:05:47 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 03:01:10 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 02:02:03 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 02:02:31 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-04-21 02:07:05 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-04-21 03:02:24 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-04-21 02:00:47 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.045 |  |
| 2026-04-21 03:02:53 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.049 |  |
| 2026-04-21 02:15:51 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.058 |  |
| 2026-04-21 02:00:09 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.120 |  |
| 2026-04-21 02:21:19 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.124 |  |
| 2026-04-21 02:11:43 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.216 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)