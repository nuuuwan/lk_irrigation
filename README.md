# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--19_03:13:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **183,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 03:13:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-19 03:09:36 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-06-19 03:09:17 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.131 |  |
| 2026-06-19 03:07:16 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:06:54 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-19 03:05:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-06-19 03:04:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-19 03:03:48 | Hanwella (Kelani Ganga) | 2.71 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-19 03:04:54 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-19 03:13:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-19 03:05:38 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-19 03:05:46 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:00:47 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:02:15 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-19 02:01:52 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:03:35 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:03:28 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:03:28 | Glencourse (Kelani Ganga) | 10.69 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:03:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:01:29 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:02:46 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:07:16 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:05:09 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-06-18 18:01:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:03:55 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-06-19 03:04:52 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-06-19 01:18:58 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.007 |  |
| 2026-06-19 03:09:36 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-06-19 03:04:56 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-06-19 03:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-06-19 03:03:13 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-06-19 02:05:37 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-06-19 03:00:52 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-06-19 03:06:04 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-06-19 03:06:54 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.019 |  |
| 2026-06-19 03:01:41 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.020 |  |
| 2026-06-19 03:05:27 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.029 |  |
| 2026-06-19 03:02:48 | Dunamale (Aththanagalu Oya) | 2.74 | 🟢 Normal | -0.033 |  |
| 2026-06-19 03:05:44 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.035 |  |
| 2026-06-18 18:04:05 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.040 |  |
| 2026-06-19 03:02:39 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.061 |  |
| 2026-06-19 03:09:17 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.131 |  |
| 2026-06-19 03:04:05 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.169 |  |
| 2026-06-19 03:04:16 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -1.500 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)