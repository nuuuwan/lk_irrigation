# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_06:12:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **213,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 06:12:57 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-23 06:08:36 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-07-23 06:08:28 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-23 06:08:13 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:07:32 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-07-23 06:06:16 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.107 |  |
| 2026-07-23 06:05:51 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-23 06:05:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:05:00 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 06:04:51 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.025 |  |
| 2026-07-23 06:04:34 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.051 |  |
| 2026-07-23 06:04:20 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-23 06:04:10 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:46 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.012 |  |
| 2026-07-23 06:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.087 |  |
| 2026-07-23 06:03:19 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:15 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-07-23 06:03:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:05 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:03 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:02 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:02:47 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.082 |  |
| 2026-07-23 06:02:44 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:02:20 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-07-23 06:02:16 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-23 06:02:15 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-23 06:01:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:26 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:24 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:18 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.008 |  |
| 2026-07-23 06:01:16 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:10 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 05:59:41 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 06:05:00 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 06:02:16 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-23 06:12:57 | Thalgahagoda (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-07-23 05:59:41 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 06:08:28 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-23 06:03:03 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:04:10 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:48 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:38 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:16 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:24 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-22 18:12:41 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:02:44 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:08:13 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:19 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:02 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:56 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:10 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:05 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:26 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:05:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:03:46 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 06:01:18 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.008 |  |
| 2026-07-23 06:08:36 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-07-23 06:04:20 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-23 06:05:51 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-07-23 06:03:15 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-07-23 06:07:32 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-07-23 06:02:20 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-07-23 06:03:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.012 |  |
| 2026-07-22 18:02:13 | Thanthirimale (Malwathu Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2026-07-23 06:02:15 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-07-23 06:04:51 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.025 |  |
| 2026-07-23 06:04:34 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.051 |  |
| 2026-07-23 06:02:47 | Glencourse (Kelani Ganga) | 9.04 | 🟢 Normal | -0.082 |  |
| 2026-07-23 06:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.087 |  |
| 2026-07-23 06:06:16 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)