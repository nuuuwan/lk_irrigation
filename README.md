# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_05:18:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,111 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 05:18:02 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-02 05:17:08 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-02 05:11:38 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.009 |  |
| 2026-06-02 05:10:40 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.014 |  |
| 2026-06-02 05:10:31 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:09:53 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-06-02 05:09:53 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-06-02 05:09:10 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.085 |  |
| 2026-06-02 05:07:13 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:06:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:05:59 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.005 |  |
| 2026-06-02 05:05:46 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-02 05:05:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-06-02 05:05:21 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.029 |  |
| 2026-06-02 05:03:59 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:03:21 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:03:17 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.031 |  |
| 2026-06-02 05:03:16 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-02 05:03:10 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:03:06 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.025 |  |
| 2026-06-02 05:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:56 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 05:02:52 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:26 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:01:29 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:01:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-02 05:01:24 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:01:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.121 |  |
| 2026-06-02 05:01:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 05:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:00:53 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:51:08 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-02 04:47:57 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.085 |  |
| 2026-06-02 04:39:09 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 03:12:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | 2.381 | 🔺 Rising |
| 2026-06-02 05:01:24 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-06-02 05:18:02 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-06-02 05:02:56 | Hanwella (Kelani Ganga) | 1.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 05:05:46 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-02 05:01:09 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 05:17:08 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-06-02 05:02:52 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:00:53 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:06:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:03:21 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:15 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:01:24 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:43 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:03:59 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:01:29 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:03:10 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:02:58 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:10:31 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:07:13 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:06:45 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-02 05:05:59 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.005 |  |
| 2026-06-02 05:11:38 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.009 |  |
| 2026-06-02 05:09:53 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-06-02 05:03:16 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:00:18 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-06-02 05:10:40 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.014 |  |
| 2026-06-02 00:06:23 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-06-02 05:09:53 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-06-02 05:03:06 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.025 |  |
| 2026-06-02 05:05:21 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.029 |  |
| 2026-06-02 05:03:17 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.031 |  |
| 2026-06-02 05:05:36 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2026-06-02 05:09:10 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.085 |  |
| 2026-06-02 05:01:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)