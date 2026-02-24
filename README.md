# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_07:01:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:29:44 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.003 |  |
| 2026-02-24 06:18:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.056 |  |
| 2026-02-24 06:17:23 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.008 |  |
| 2026-02-24 06:12:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.222 |  |
| 2026-02-24 06:10:45 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:08:57 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | -0.052 |  |
| 2026-02-24 06:08:53 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-02-24 06:08:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-24 06:08:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:08:12 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.072 |  |
| 2026-02-24 06:07:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:07:02 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-02-24 06:06:56 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 06:07:02 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-02-24 06:04:28 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-24 06:08:20 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-24 06:06:56 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-24 06:01:26 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:02:48 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 07:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:02:41 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:10:45 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:04:14 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:02:29 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:02:24 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:08:14 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:04:05 | Badalgama (Maha Oya) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:07:07 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:01:37 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:02:46 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 06:29:44 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.003 |  |
| 2026-02-24 06:04:10 | Weraganthota (Mahaweli Ganga) | -2.00 | 🟢 Normal | -0.007 |  |
| 2026-02-24 06:17:23 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.008 |  |
| 2026-02-24 06:03:55 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-24 06:08:53 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2026-02-24 06:02:56 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-24 06:02:54 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-02-24 06:04:02 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-24 06:03:16 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-02-24 06:03:02 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.021 |  |
| 2026-02-24 06:01:50 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | -0.030 |  |
| 2026-02-24 06:02:20 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-02-24 06:04:21 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.032 |  |
| 2026-02-24 06:05:45 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2026-02-24 06:08:57 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | -0.052 |  |
| 2026-02-24 06:18:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.056 |  |
| 2026-02-24 06:02:15 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.062 |  |
| 2026-02-24 06:08:12 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | -0.072 |  |
| 2026-02-24 06:12:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.222 |  |
| 2026-02-24 06:02:01 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.308 |  |
| 2026-02-24 06:02:49 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)