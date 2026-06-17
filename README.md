# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_00:00:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,207 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **4** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 00:00:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:38:15 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-17 23:12:13 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-17 23:11:21 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-17 23:01:23 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | 0.705 | 🔺 Rising |
| 2026-06-17 23:12:13 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-06-17 23:02:53 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-06-17 23:05:47 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-06-17 23:04:32 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-17 23:03:15 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-06-17 23:03:38 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-17 23:06:38 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-17 23:04:22 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-17 23:08:56 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-17 23:38:15 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-17 23:01:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.005 |  |
| 2026-06-17 23:05:06 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.005 |  |
| 2026-06-17 18:02:56 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 21:07:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:26 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:39 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:05:15 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:00:39 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:30 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:03:31 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:06:37 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:06 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:26 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:46 | Dunamale (Aththanagalu Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-06-18 00:00:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:02:39 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:06:59 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-06-17 23:01:13 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-17 18:05:17 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-06-17 18:01:25 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-06-17 23:01:22 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-06-17 21:10:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.022 |  |
| 2026-06-17 23:11:21 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.028 |  |
| 2026-06-17 23:06:55 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.077 |  |
| 2026-06-17 23:07:27 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.087 |  |
| 2026-06-17 23:04:15 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.089 |  |
| 2026-06-17 23:03:20 | Rathnapura (Kalu Ganga) | 3.12 | 🟢 Normal | -0.105 |  |
| 2026-06-17 23:04:05 | Deraniyagala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)