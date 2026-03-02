# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_13:03:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,176 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 13:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-03-02 13:03:35 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-02 13:03:22 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-03-02 13:03:08 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:03:07 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-02 13:02:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:40 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:29 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:02:20 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | -0.040 |  |
| 2026-03-02 13:02:16 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.052 |  |
| 2026-03-02 13:02:08 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:03 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:50 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:40 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.172 |  |
| 2026-03-02 13:01:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:25 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:21 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:01:21 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 13:01:19 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:11 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-02 13:01:08 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:00:57 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.013 |  |
| 2026-03-02 13:00:45 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:00:21 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-02 13:00:12 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:14:31 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.013 |  |
| 2026-03-02 12:14:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:11:04 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-03-02 12:09:29 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:08:53 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.058 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 13:02:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-02 13:00:21 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-02 13:03:35 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-02 12:02:53 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-02 12:06:00 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-02 13:01:21 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 13:01:11 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-02 12:08:27 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 12:07:54 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:50 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:00:12 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:25 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:06:33 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:03 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:04:43 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:08 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:00:45 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 11:26:22 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:02:40 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:13 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:26 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:02:47 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:14:25 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:03:07 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:07:13 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 13:01:19 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-02 12:11:04 | Horowpothana (Yan Oya) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-03-02 13:03:08 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:01:21 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:02:29 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:01:08 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-02 13:00:57 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.013 |  |
| 2026-03-02 13:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-03-02 13:03:22 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.020 |  |
| 2026-03-02 13:02:20 | Dunamale (Aththanagalu Oya) | 0.28 | 🟢 Normal | -0.040 |  |
| 2026-03-02 13:02:16 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | -0.052 |  |
| 2026-03-02 13:01:40 | Weraganthota (Mahaweli Ganga) | -1.96 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)