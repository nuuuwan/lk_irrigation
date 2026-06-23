# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_01:31:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,644 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 01:31:23 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:11:10 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-24 01:08:48 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.009 |  |
| 2026-06-24 01:06:51 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-06-24 01:06:27 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-24 01:06:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-24 01:06:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 00:20:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.006 |  |
| 2026-06-24 01:02:41 | Dunamale (Aththanagalu Oya) | 3.55 | 🟡 Alert | -0.050 |  |
| 2026-06-24 01:06:23 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-24 01:04:41 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:02:23 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:00:57 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:00:10 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:31:23 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:04:17 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:03:23 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:03:34 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:06:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 00:05:36 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:04:56 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:03:37 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 01:11:10 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-06-24 01:08:48 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.009 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-24 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-24 01:05:39 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-24 01:03:53 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.013 |  |
| 2026-06-24 00:11:59 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.018 |  |
| 2026-06-24 01:06:51 | Thawalama (Gin Ganga) | 1.91 | 🟢 Normal | -0.019 |  |
| 2026-06-24 01:06:27 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-06-24 01:05:38 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.031 |  |
| 2026-06-24 01:00:38 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | -0.031 |  |
| 2026-06-24 01:02:59 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.031 |  |
| 2026-06-24 00:22:14 | Magura (Kalu Ganga) | 2.50 | 🟢 Normal | -0.039 |  |
| 2026-06-24 00:03:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.046 |  |
| 2026-06-24 01:03:06 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-06-24 01:00:37 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-06-24 01:02:13 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | -0.064 |  |
| 2026-06-24 00:01:14 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.076 |  |
| 2026-06-24 01:04:07 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.082 |  |
| 2026-06-24 01:05:01 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.094 |  |
| 2026-06-24 01:01:01 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | -3.180 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)