# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_18:16:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,451 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 18:16:34 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 18:15:18 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:11:51 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-07-02 18:10:12 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-07-02 18:07:38 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.013 |  |
| 2026-07-02 18:07:32 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:07:29 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:06:31 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.046 |  |
| 2026-07-02 18:06:21 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:05:29 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:05:08 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:04:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-02 18:03:35 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:03:35 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:03:29 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-07-02 18:03:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:03:11 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-07-02 18:03:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |
| 2026-07-02 18:02:40 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:02:32 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:02:15 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:02:11 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:02:11 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.061 |  |
| 2026-07-02 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-07-02 18:02:03 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:56 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.062 |  |
| 2026-07-02 18:01:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:28 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.020 |  |
| 2026-07-02 18:01:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:17 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:03 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:00:42 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:38 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:25 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 18:04:44 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-02 18:02:03 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-02 18:16:34 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:25 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:26 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:38 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:15:18 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:58 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:00:42 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:03:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:02:32 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:17 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:05:08 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:07:32 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:03:35 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 16:01:24 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:02:40 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:07:29 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:02:11 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:01:28 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:06:21 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 18:11:51 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-07-02 18:10:12 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-07-02 18:02:15 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:05:29 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:03:35 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:01:03 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-07-02 18:03:29 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2026-07-02 18:07:38 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.013 |  |
| 2026-07-02 18:01:28 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | -0.020 |  |
| 2026-07-02 18:03:11 | Hanwella (Kelani Ganga) | 1.54 | 🟢 Normal | -0.020 |  |
| 2026-07-02 18:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.38 | 🟢 Normal | -0.040 |  |
| 2026-07-02 18:06:31 | Glencourse (Kelani Ganga) | 9.58 | 🟢 Normal | -0.046 |  |
| 2026-07-02 18:02:11 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.061 |  |
| 2026-07-02 18:01:56 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.062 |  |
| 2026-07-02 18:03:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)