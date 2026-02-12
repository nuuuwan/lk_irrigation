# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_01:13:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,492 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 01:13:14 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:07:09 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:05:55 | Peradeniya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.039 |  |
| 2026-02-13 01:05:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-02-13 01:05:01 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | 0.447 | 🔺 Rising |
| 2026-02-13 01:04:02 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 01:03:53 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 01:03:38 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-13 01:03:27 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-13 01:03:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:03:14 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 01:03:13 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:02:36 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:02:18 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:01:29 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-13 01:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:01:21 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:01:20 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:00:32 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-02-13 01:00:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 01:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.10 | 🟢 Normal | 0.447 | 🔺 Rising |
| 2026-02-13 01:01:29 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-12 23:04:31 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-13 00:06:41 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-12 22:47:15 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-13 00:03:25 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 23:05:18 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-13 01:03:14 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 01:04:02 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 00:10:12 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 01:03:53 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 22:09:35 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 01:00:10 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:02:36 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:01:21 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:01:20 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 00:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-13 00:02:28 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:02:18 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 00:22:23 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-13 00:18:03 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:03:25 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-13 00:05:23 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:21:10 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:05:01 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-02-12 23:04:13 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:13:14 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:03:13 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:07:09 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:01:23 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 01:03:27 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-13 01:03:38 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-13 00:05:27 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-02-13 01:00:32 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-02-13 01:05:18 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-02-13 01:05:55 | Peradeniya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)