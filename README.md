# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_15:16:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **77,387 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 15:16:28 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:09:55 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:09:26 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:08:15 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:06:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:06:06 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.012 |  |
| 2026-02-19 15:05:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:05:00 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:04:18 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 15:01:53 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-02-19 15:03:33 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-19 15:01:14 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-19 15:00:10 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-19 15:02:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-19 15:00:42 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-19 15:02:41 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 15:01:59 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 15:04:18 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 15:03:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:02:22 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:03:39 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:00:07 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:16:28 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:09:26 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:08:15 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:09:55 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:01:35 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:02:38 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:03:04 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:01:46 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:06:50 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:02:22 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:05:00 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:05:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:01:30 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-19 15:03:38 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-02-19 15:02:29 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-19 15:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-02-19 15:00:34 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-19 15:03:25 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-02-19 15:06:06 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.012 |  |
| 2026-02-19 15:02:43 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.013 |  |
| 2026-02-19 14:05:18 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-02-19 15:02:33 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.032 |  |
| 2026-02-19 15:02:55 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.040 |  |
| 2026-02-19 15:02:23 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.047 |  |
| 2026-02-19 15:02:46 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.052 |  |
| 2026-02-19 15:02:06 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)