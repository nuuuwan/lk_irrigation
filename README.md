# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_04:18:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,693 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 04:18:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:15:42 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-04-03 04:13:20 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:12:17 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:11:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:11:05 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:09:39 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-03 04:09:38 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-03 04:09:34 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.014 |  |
| 2026-04-03 04:09:10 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-04-03 04:09:08 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-04-03 04:06:03 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 04:05:53 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:05:47 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:04:27 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:57 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 04:03:42 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:35 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:33 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-04-03 04:03:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:12 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:02:42 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-04-03 04:02:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:02:22 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-03 04:02:18 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:02:17 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:41 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:41 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:37 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:29 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 04:01:16 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-03 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:00:18 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.183 |  |
| 2026-04-03 03:42:43 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.273 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 04:09:10 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 54.000 | 🔺 Rising |
| 2026-04-03 04:15:42 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-04-03 04:02:42 | Kithulgala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-04-03 04:09:39 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-03 04:02:22 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-04-03 04:03:57 | Ellagawa (Kalu Ganga) | 3.72 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 04:01:29 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 03:06:11 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 04:06:03 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 04:11:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:02:18 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 03:02:15 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:02:17 | Giriulla (Maha Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:41 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:35 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:18:22 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:02:42 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:12:17 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:13:20 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:05:47 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:42 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:37 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:04:27 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:05:53 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:12 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:01:41 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:11:05 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 02:20:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:09:38 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-03 04:01:16 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-03 04:09:34 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.014 |  |
| 2026-04-03 00:02:54 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-03 04:03:33 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.040 |  |
| 2026-04-03 04:00:18 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.183 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)