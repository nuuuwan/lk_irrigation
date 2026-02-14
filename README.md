# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--14_07:00:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 07:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 06:36:11 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-14 06:32:58 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.002 |  |
| 2026-02-14 06:32:52 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:14:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.013 |  |
| 2026-02-14 06:10:40 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:08:04 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:07:58 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-02-14 06:07:21 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:40 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:31 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:25 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.020 |  |
| 2026-02-14 06:06:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -19.915 |  |
| 2026-02-14 06:06:09 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-14 06:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -19.915 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-14 06:01:08 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.498 | 🔺 Rising |
| 2026-02-14 06:04:30 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-14 06:36:11 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-14 06:02:27 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-14 06:04:20 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-14 07:00:07 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 06:03:20 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 06:03:16 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.002 |  |
| 2026-02-14 06:32:58 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.002 |  |
| 2026-02-14 06:02:30 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:05:53 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:04:16 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:01:35 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:07:21 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:03:01 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:03:55 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:08:04 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:40 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:02:30 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:10:40 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:31 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:31 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:03:09 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:32:52 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:02:38 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:04:55 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-02-14 06:06:09 | Dunamale (Aththanagalu Oya) | 0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-14 06:00:34 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-14 06:14:19 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.013 |  |
| 2026-02-14 06:07:58 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-02-14 06:06:25 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.020 |  |
| 2026-02-14 06:00:42 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.022 |  |
| 2026-02-14 06:01:46 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.023 |  |
| 2026-02-14 06:04:11 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.024 |  |
| 2026-02-14 06:04:19 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.031 |  |
| 2026-02-14 06:01:24 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.031 |  |
| 2026-02-14 06:00:12 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.206 |  |
| 2026-02-14 06:06:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -19.915 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)