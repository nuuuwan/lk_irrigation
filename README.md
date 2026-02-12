# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_23:06:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,437 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 23:06:12 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:06:07 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-12 23:05:40 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-12 23:05:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:05:18 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 23:05:12 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:05:05 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.005 |  |
| 2026-02-12 23:04:47 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:04:46 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:04:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-12 23:04:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:32 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:03:30 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:23 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:17 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:05 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:02:58 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-12 23:02:37 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-12 23:02:14 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-12 23:02:08 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-02-12 23:01:55 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:01:44 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:01:34 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.040 |  |
| 2026-02-12 23:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 23:01:01 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:00:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:00:42 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-02-12 22:47:15 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-12 22:23:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-12 22:22:53 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 22:18:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:17:05 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:16:10 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 22:13:16 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.059 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 22:23:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-02-12 23:05:40 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-12 23:02:37 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-12 23:04:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-12 22:16:10 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-02-12 23:06:07 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-12 23:02:58 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-12 22:47:15 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-12 22:10:11 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-12 23:05:18 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 23:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 22:05:00 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:01:55 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:03:05 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:03:32 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 22:09:35 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 23:01:01 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:30 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:01:44 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:05:12 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:00:50 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:23 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:06:12 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:05:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:04:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:06 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:04:47 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:04:46 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:03:17 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:09:16 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-12 22:18:25 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:05:05 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.005 |  |
| 2026-02-12 23:02:14 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-12 23:02:08 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-02-12 23:00:42 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-02-12 23:01:34 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)