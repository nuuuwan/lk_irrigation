# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_04:08:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,074 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 04:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:07:11 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-06-02 04:06:45 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:06:40 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.151 |  |
| 2026-06-02 04:05:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-06-02 04:05:25 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:04:32 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:04:08 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:03:53 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-02 04:03:32 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:03:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 04:03:20 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 04:03:19 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:03:19 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 04:03:08 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:03:03 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-02 04:02:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:02:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:01:47 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:01:35 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:01:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:42 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:20 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:18 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-06-02 04:00:16 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 03:12:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | 2.381 | 🔺 Rising |
| 2026-06-02 04:03:03 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-02 04:03:53 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-06-02 03:01:40 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-06-02 03:02:32 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-02 04:03:26 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 04:03:19 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 04:03:20 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:16 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:03:19 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:01:47 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-02 03:02:33 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:20 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:02:13 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:02:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:01:35 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:00:42 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:05:25 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:01:20 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 03:04:53 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-06-02 03:02:25 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-02 03:05:36 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:06:45 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-02 04:04:32 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:03:32 | Rathnapura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:04:08 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:03:08 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | -0.010 |  |
| 2026-06-02 04:00:18 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-06-02 03:02:57 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.015 |  |
| 2026-06-02 00:06:23 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | -0.019 |  |
| 2026-06-02 03:12:54 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.025 |  |
| 2026-06-02 04:07:11 | Baddegama (Gin Ganga) | 1.63 | 🟢 Normal | -0.031 |  |
| 2026-06-02 04:05:53 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-06-02 04:06:40 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)