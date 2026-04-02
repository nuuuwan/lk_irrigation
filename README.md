# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_05:12:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,727 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 05:12:55 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-04-03 05:11:59 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:09:31 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.109 |  |
| 2026-04-03 05:09:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 05:07:21 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 05:07:02 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.066 |  |
| 2026-04-03 05:06:48 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:06:25 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-03 05:06:21 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.118 |  |
| 2026-04-03 05:06:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:06:02 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:05:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-04-03 05:05:20 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:03:25 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.029 |  |
| 2026-04-03 05:03:24 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 05:03:23 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 05:03:06 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:53 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:41 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-03 05:02:29 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:26 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 05:02:18 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.077 |  |
| 2026-04-03 05:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:49 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:19 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 05:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-03 05:01:08 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:00:47 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-03 04:37:45 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:37:18 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:36:56 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:36:39 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 05:02:41 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-04-03 05:06:25 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-03 05:00:47 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-03 05:07:21 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 05:03:23 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 05:03:24 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-03 05:01:19 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 05:02:26 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 05:09:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 05:03:06 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:11:58 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:53 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:49 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:11:59 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:03:35 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:08 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:12:17 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:05:20 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:06:02 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:29 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:02:44 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:06:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:06:48 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:01:49 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-04-03 04:11:05 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 02:20:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-03 05:12:55 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-04-03 05:01:09 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-03 04:01:16 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.011 |  |
| 2026-04-03 05:03:25 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.029 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-03 05:05:51 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.061 |  |
| 2026-04-03 05:07:02 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.066 |  |
| 2026-04-03 05:02:18 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.077 |  |
| 2026-04-03 05:09:31 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.109 |  |
| 2026-04-03 05:06:21 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)