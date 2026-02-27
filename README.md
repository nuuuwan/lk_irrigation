# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_02:46:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **84,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 02:46:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:45:53 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:32:29 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:22:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-28 02:12:19 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:12:00 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:11:38 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:09:58 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:09:54 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:08:08 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-02-28 02:07:38 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:07:29 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-28 02:07:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-28 02:05:50 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:04:25 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-28 02:03:34 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:32 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:27 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-28 02:03:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:02:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:02:13 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:01:55 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:01:44 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.072 |  |
| 2026-02-28 02:01:31 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:01:10 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:00:57 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:00:53 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 02:07:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-28 02:00:53 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-28 02:04:25 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-28 02:07:29 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-28 01:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 02:22:08 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-28 00:09:52 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:01:10 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:00:57 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:34 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:26 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-28 01:37:11 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:13:29 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 01:17:33 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-28 01:01:32 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-28 01:04:16 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:01:31 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:46:41 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:01:55 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:05:50 | Dunamale (Aththanagalu Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:32 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:02:50 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 00:28:44 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:03:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:07:38 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:09:58 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-27 18:03:42 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:32:29 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:12:19 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:02:13 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-28 02:08:08 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2026-02-28 02:03:27 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-28 01:01:12 | Manampitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-02-28 01:54:56 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-02-27 18:05:48 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.028 |  |
| 2026-02-28 02:01:44 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.072 |  |
| 2026-02-27 22:00:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.087 |  |
| 2026-02-28 01:01:56 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)