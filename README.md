# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_17:00:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,273 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 17:00:57 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.060 |  |
| 2026-04-02 17:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-02 17:00:21 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:59:21 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-04-02 16:25:44 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-02 16:19:53 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:17:10 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.008 |  |
| 2026-04-02 16:14:43 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:09:32 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 16:07:30 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-02 16:07:19 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 17:00:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-02 16:03:48 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-02 16:07:30 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-02 16:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-02 16:03:50 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-02 16:02:59 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-02 16:00:10 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 16:02:22 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 16:03:12 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 16:00:54 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 16:07:19 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 16:09:32 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 16:06:17 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:04:18 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:14:43 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:01:32 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:03:15 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:19:53 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:02:51 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:03:32 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:03:32 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:00:14 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:21 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:05:04 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:02:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:05:11 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:05:51 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:06:15 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:17:10 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.008 |  |
| 2026-04-02 16:02:52 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-02 16:59:21 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-04-02 16:03:22 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.020 |  |
| 2026-04-02 16:03:00 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.021 |  |
| 2026-04-02 16:00:11 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-04-02 16:01:51 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.052 |  |
| 2026-04-02 17:00:57 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.060 |  |
| 2026-04-02 16:01:42 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)