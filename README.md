# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_09:07:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 09:07:04 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 09:06:37 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:06:11 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:05:46 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 09:04:33 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:29 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:23 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 09:04:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:16 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:00 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.087 |  |
| 2026-02-19 09:03:26 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.160 |  |
| 2026-02-19 09:03:25 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.020 |  |
| 2026-02-19 09:03:16 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-19 09:03:05 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 09:03:01 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:42 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 09:02:39 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-02-19 09:02:38 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:30 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:23 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.030 |  |
| 2026-02-19 09:02:18 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-19 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.040 |  |
| 2026-02-19 09:02:01 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:01:41 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:01:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-19 09:01:31 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-02-19 09:01:26 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 09:00:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:00:34 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:00:16 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-19 08:19:38 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:16:00 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.013 |  |
| 2026-02-19 08:15:24 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:13:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 09:01:31 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-02-19 09:01:41 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-19 09:05:46 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 09:03:05 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 09:01:26 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 09:02:42 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 09:04:23 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 09:07:04 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-19 09:02:01 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:06:11 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:00:34 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:05:52 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:33 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:18 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:06:37 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:02:36 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:00:34 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:38 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:30 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:09:23 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:00:59 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:29 | Dunamale (Aththanagalu Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:03:01 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:13:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:58 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 08:06:07 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:01:41 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:04:16 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 09:02:18 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-19 09:03:16 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-19 09:00:16 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-19 09:02:39 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.013 |  |
| 2026-02-19 09:03:25 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.020 |  |
| 2026-02-19 09:02:23 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.030 |  |
| 2026-02-19 09:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | -0.040 |  |
| 2026-02-19 08:07:17 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-02-19 09:04:00 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.087 |  |
| 2026-02-19 09:03:26 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)