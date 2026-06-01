# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_02:07:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,002 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 02:07:43 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:06:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:06:53 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-06-02 02:04:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-02 02:04:37 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.048 |  |
| 2026-06-02 02:04:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:03:57 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:03:30 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-02 02:03:29 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:03:20 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-06-02 02:03:02 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:02:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:02:26 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-06-02 02:02:20 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:01:58 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:01:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 02:01:27 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-06-02 02:01:24 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-02 02:00:52 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:00:49 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:00:23 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.011 |  |
| 2026-06-02 01:56:32 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-06-02 01:33:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 01:26:20 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 02:04:41 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-01 23:25:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-02 01:03:40 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-02 02:01:30 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 01:01:10 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 02:02:35 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:00:52 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:00:49 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:02:20 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:01:41 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 01:33:32 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:03:02 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:03:29 | Hanwella (Kelani Ganga) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:04:16 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-02 00:04:33 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:03:57 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:01:58 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 01:05:16 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:06:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-02 00:03:59 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-02 01:00:50 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 01:02:33 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:07:43 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-02 02:01:24 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-06-02 02:03:30 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-06-02 02:01:27 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-06-02 02:00:23 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | -0.011 |  |
| 2026-06-02 00:06:23 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-06-02 01:56:32 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.020 |  |
| 2026-06-02 02:06:53 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2026-06-02 01:05:23 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.021 |  |
| 2026-06-02 01:02:07 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | -0.025 |  |
| 2026-06-02 02:03:20 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-06-02 02:02:26 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.039 |  |
| 2026-06-02 02:04:37 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)